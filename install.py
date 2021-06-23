import os
import time

list = ['cairo', 'curl', 'docbook', 'docbook-xsl', 'fontconfig', 'fontforge', 
'freetds', 'freetype', 'fribidi', 'gd', 'gdbm', 'gettext', 'ghostscript', 'giflib', 
'glib', 'gmp', 'gnu-getopt', 'gobject-introspection', 'graphite2', 'harfbuzz', 
'icu4c', 'ilmbase', 'imagemagick', 'imath', 'jbig2dec', 'jemalloc', 'jpeg', 
'krb5', 'libde265', 'libev', 'libevent', 'libffi', 'libheif', 'libidn', 
'libidn2', 'liblqr', 'libmemcached', 'libmetalink', 'libomp', 'libpng', 
'libpq', 'libpthread-stubs', 'libsodium', 'libspiro', 'libssh2', 'libtiff', 
'libtool', 'libuninameslist', 'libunistring', 'libx11', 'libxau', 'libxcb', 
'libxdmcp', 'libxext', 'libxrender', 'libzip', 'little-cms2', 'lzo', 'm4', 
'mpdecimal', 'msodbcsql17', 'mssql-tools', 'mysql-client', 'ncurses', 'neofetch', 
'nghttp2', 'oniguruma', 'openexr', 'openjpeg', 'openldap', 'openssl@1.1', 'pango', 
'pcre', 'pcre2', 'php@7.2', 'php@7.3', 'pixman', 'pkg-config', 'putty', 'python@3.8', 
'python@3.9', 'readline', 'rtmpdump', 'screenresolution', 'shared-mime-info', 'sqlite', 
'tcl-tk', 'telnet', 'tidy-html5', 'unixodbc', 'watch', 'webp', 'wget', 'x265', 'xmlto', 
'xorgproto', 'xz', 'zsh-syntax-highlighting', 'zstd', 'chromedriver', 'iterm2']

for i in list:
    os.system('arch -arm64 brew install ' + i)
    time.sleep(1)



# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
# arch -arm64 brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
# brew update
# HOMEBREW_NO_ENV_FILTERING=1 ACCEPT_EULA=Y brew install msodbcsql17 mssql-tools
