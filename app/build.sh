#!/bin/bash
set -euo pipefail

rm -rf temp dist build *.so *.pyd
mkdir -p temp

export CFLAGS="-O3 -march=native -flto -fno-semantic-interposition -fomit-frame-pointer"
export LDFLAGS="-O3 -flto -Wl,--as-needed"

pip install --no-cache-dir -r requirements.txt || echo "no requirements.txt found"
pip install --no-cache-dir --upgrade cython setuptools pyinstaller

python setup.py build_ext \
    --build-lib=temp \
    --build-temp=temp/build_cython \
    --inplace \
    --force

python -m PyInstaller \
    -n imageshop \
    --clean \
    --strip \
    -d noarchive \
    --optimize 2 \
    --onefile main.py \
    --distpath=./dist \
    --log-level=ERROR \
    --runtime-tmpdir=. \
    --exclude-module ssl \
    --exclude-module lzma \
    --exclude-module pytest \
    --exclude-module curses \
    --exclude-module sqlite3 \
    --exclude-module tkinter \
    --exclude-module unittest \
    --exclude-module multiprocessing \
    --exclude-module=pyi_rth_inspect \
    --workpath=temp/build_pyinstaller \

mv *.so ./temp/ || echo "no modules files found, continuing"
rm -rf *.spec

# upx unneeded
# echo -e "\nuse upx compression? [Y/n]"
# read -r CONTINUE
# if [[ ! "$CONTINUE" =~ ^[Nn]$ ]]; then
#     if command -v upx &> /dev/null; then
#         echo "compressing with upx..."
#         upx --best --lzma --compress-icons=0 dist/imageshop
#     else
#         echo "upx not found, skipping compression"
#     fi 
# fi

strip --strip-all -R .comment -R .note -R .gnu.version dist/imageshop
objcopy --strip-unneeded \
        --remove-section=.note* \
        --remove-section=.comment \
        dist/imageshop

echo -e "\nfinal executable size:"
du -sh dist/imageshop
file dist/imageshop

# determine install path based on architecture
if [[ "$(uname -s | tr '[:upper:]' '[:lower:]')" == "darwin" ]]; then
    INSTALL_PATH='/usr/local/bin/'
else
    INSTALL_PATH='/usr/bin/'
fi

echo -e "\ninstall to ${INSTALL_PATH}? [Y/n]"
read -r CONTINUE
if [[ "$CONTINUE" =~ ^[Nn]$ ]]; then
    echo "executable available at: $(pwd)/dist/imageshop"
else
    sudo mv "dist/imageshop" "${INSTALL_PATH}imageshop"
    echo "installed to ${INSTALL_PATH}imageshop"
fi

echo "uninstall with 'sudo rm -rf ${INSTALL_PATH}imageshop'"

rm -rf __pycache__/ build/ temp/