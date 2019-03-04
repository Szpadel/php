#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD66C9593118BCCB6 (cmb@php.net)
#
Name     : php
Version  : 7.3.2
Release  : 158
URL      : https://php.net/distributions/php-7.3.2.tar.xz
Source0  : https://php.net/distributions/php-7.3.2.tar.xz
Source99 : https://php.net/distributions/php-7.3.2.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause HPND LGPL-2.1 MIT OLDAP-2.8 PHP-3.01 Zend-2.0 Zlib
Requires: php-bin = %{version}-%{release}
Requires: php-data = %{version}-%{release}
Requires: php-lib = %{version}-%{release}
Requires: php-license = %{version}-%{release}
Requires: php-man = %{version}-%{release}
Requires: php-services = %{version}-%{release}
BuildRequires : argon2-dev
BuildRequires : aspell-dev
BuildRequires : bison
BuildRequires : bzip2-dev
BuildRequires : ca-certs
BuildRequires : curl-dev
BuildRequires : db
BuildRequires : dbus-dev
BuildRequires : e2fsprogs-dev
BuildRequires : enchant-dev
BuildRequires : expat-dev
BuildRequires : file-dev
BuildRequires : freetype
BuildRequires : freetype-dev
BuildRequires : gdbm-dev
BuildRequires : gettext-dev
BuildRequires : gmp-dev
BuildRequires : httpd-dev
BuildRequires : krb5-dev
BuildRequires : libXpm-dev
BuildRequires : libgd-dev
BuildRequires : libidn-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : libxml2
BuildRequires : libxml2-dev
BuildRequires : libxslt-dev
BuildRequires : libzip-dev
BuildRequires : lmdb-dev
BuildRequires : mariadb-dev
BuildRequires : ncurses-dev
BuildRequires : nghttp2-dev
BuildRequires : onig-dev
BuildRequires : openssl-dev
BuildRequires : pcre-dev
BuildRequires : php
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libpq)
BuildRequires : pkgconfig(libwebp)
BuildRequires : postgresql-dev
BuildRequires : re2c
BuildRequires : readline-dev
BuildRequires : systemd-dev
BuildRequires : valgrind
BuildRequires : xz-dev
BuildRequires : zlib-dev
Patch1: cve-2017-11146.nopatch
Patch2: 0001-configure-php-fpm-service.patch
Patch3: 0002-disable-php-openssl-ext-rc4-algo.patch
Patch4: 0003-reduce-fpm-event-wakeups.patch

%description
PHP

%package bin
Summary: bin components for the php package.
Group: Binaries
Requires: php-data = %{version}-%{release}
Requires: php-license = %{version}-%{release}
Requires: php-man = %{version}-%{release}
Requires: php-services = %{version}-%{release}

%description bin
bin components for the php package.


%package data
Summary: data components for the php package.
Group: Data

%description data
data components for the php package.


%package dev
Summary: dev components for the php package.
Group: Development
Requires: php-lib = %{version}-%{release}
Requires: php-bin = %{version}-%{release}
Requires: php-data = %{version}-%{release}
Provides: php-devel = %{version}-%{release}

%description dev
dev components for the php package.


%package lib
Summary: lib components for the php package.
Group: Libraries
Requires: php-data = %{version}-%{release}
Requires: php-license = %{version}-%{release}

%description lib
lib components for the php package.


%package license
Summary: license components for the php package.
Group: Default

%description license
license components for the php package.


%package man
Summary: man components for the php package.
Group: Default

%description man
man components for the php package.


%package services
Summary: services components for the php package.
Group: Systemd services

%description services
services components for the php package.


%prep
%setup -q -n php-7.3.2
cd ..
%setup -q -T -D -n php-7.3.2 -b 1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550629031
export LDFLAGS="${LDFLAGS} -fno-lto"
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=pgo -fprofile-update=atomic "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" %configure --disable-static --sysconfdir=/usr/share/defaults/php \
--enable-dba=shared \
--enable-calendar \
--enable-ftp \
--enable-soap \
--enable-sockets \
--with-gd \
--enable-zip \
--with-curl \
--enable-pcntl \
--with-bz2 \
--with-zlib \
--with-gmp \
--enable-phar \
--enable-fpm \
--with-fpm-systemd \
--with-mysql=mysqlnd \
--with-mysqli=mysqlnd \
--with-pdo-mysql=mysqlnd \
--with-pgsql \
--with-pdo-pgsql \
--with-mysql-sock=/run/mariadb/mariadb.sock \
--without-readline \
--enable-mbstring \
--with-openssl \
--enable-sysvmsg \
--with-onig=/usr \
--with-system-ciphers \
--enable-opcache \
--enable-pcre-jit \
--enable-re2c-cgoto \
--with-config-file-path=/usr/share/defaults/php/ \
--with-jpeg-dir=/usr/lib64 \
--with-webp-dir=/usr/lib64 \
--with-kerberos \
--enable-calendar \
--enable-exif \
--with-password-argon2 \
--enable-bcmath \
--with-lmdb \
--with-gdbm \
--with-xsl=/usr/lib64/ \
--with-gettext \
--enable-intl \
--with-readline
make  %{?_smp_mflags}

export NO_INTERACTION=1 SKIP_ONLINE_TESTS=1
make test || :
make clean
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" %configure --disable-static --sysconfdir=/usr/share/defaults/php \
--enable-dba=shared \
--enable-calendar \
--enable-ftp \
--enable-soap \
--enable-sockets \
--with-gd \
--enable-zip \
--with-curl \
--enable-pcntl \
--with-bz2 \
--with-zlib \
--with-gmp \
--enable-phar \
--enable-fpm \
--with-fpm-systemd \
--with-mysql=mysqlnd \
--with-mysqli=mysqlnd \
--with-pdo-mysql=mysqlnd \
--with-pgsql \
--with-pdo-pgsql \
--with-mysql-sock=/run/mariadb/mariadb.sock \
--without-readline \
--enable-mbstring \
--with-openssl \
--enable-sysvmsg \
--with-onig=/usr \
--with-system-ciphers \
--enable-opcache \
--enable-pcre-jit \
--enable-re2c-cgoto \
--with-config-file-path=/usr/share/defaults/php/ \
--with-jpeg-dir=/usr/lib64 \
--with-webp-dir=/usr/lib64 \
--with-kerberos \
--enable-calendar \
--enable-exif \
--with-password-argon2 \
--enable-bcmath \
--with-lmdb \
--with-gdbm \
--with-xsl=/usr/lib64/ \
--with-gettext \
--enable-intl \
--with-readline
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1550629031
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/php
cp TSRM/LICENSE %{buildroot}/usr/share/package-licenses/php/TSRM_LICENSE
cp Zend/LICENSE %{buildroot}/usr/share/package-licenses/php/Zend_LICENSE
cp ext/bcmath/libbcmath/COPYING.LIB %{buildroot}/usr/share/package-licenses/php/ext_bcmath_libbcmath_COPYING.LIB
cp ext/date/lib/LICENSE.rst %{buildroot}/usr/share/package-licenses/php/ext_date_lib_LICENSE.rst
cp ext/fileinfo/libmagic/LICENSE %{buildroot}/usr/share/package-licenses/php/ext_fileinfo_libmagic_LICENSE
cp ext/mbstring/libmbfl/LICENSE %{buildroot}/usr/share/package-licenses/php/ext_mbstring_libmbfl_LICENSE
cp ext/mbstring/oniguruma/COPYING %{buildroot}/usr/share/package-licenses/php/ext_mbstring_oniguruma_COPYING
cp ext/mbstring/ucgendat/OPENLDAP_LICENSE %{buildroot}/usr/share/package-licenses/php/ext_mbstring_ucgendat_OPENLDAP_LICENSE
cp ext/zip/LICENSE_libzip %{buildroot}/usr/share/package-licenses/php/ext_zip_LICENSE_libzip
cp sapi/fpm/LICENSE %{buildroot}/usr/share/package-licenses/php/sapi_fpm_LICENSE
%make_install
## install_append content
mkdir -p %{buildroot}/usr/lib64/php/docs
mv %{buildroot}/usr/lib64/php/doc/PEAR %{buildroot}/usr/lib64/php/docs/PEAR
mv %{buildroot}/usr/share/defaults/php/php-fpm.conf.default %{buildroot}/usr/share/defaults/php/php-fpm.conf
install -D -m 644 config/php-fpm.service %{buildroot}/usr/lib/systemd/system/php-fpm.service
install -D -m 644 config/php-httpd.conf %{buildroot}/usr/share/defaults/httpd/conf.d/php.conf
rm -rf %{buildroot}/.depdb* %{buildroot}/.lock %{buildroot}/.channels %{buildroot}/.filemap
mv %{buildroot}/usr/share/defaults/php/php-fpm.d/www.conf.default %{buildroot}/usr/share/defaults/php/php-fpm.d/www.conf
mkdir -p %{buildroot}/usr/share/defaults/php
cat > %{buildroot}/usr/share/defaults/php/php.ini  <<_ASUNAME
[zendopcache]
zend_extension=/usr/lib64/extensions/no-debug-non-zts-20180731/opcache.so
opcache.memory_consumption=128
opcache.interned_strings_buffer=8
opcache.max_accelerated_files=4000
opcache.revalidate_freq=180
opcache.fast_shutdown=1
opcache.enable_cli=1
_ASUNAME
mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -sf /usr/lib/systemd/system/php-fpm.service %{buildroot}/usr/share/clr-service-restart/php-fpm.service
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/build/Makefile.global
/usr/lib64/build/acinclude.m4
/usr/lib64/build/ax_check_compile_flag.m4
/usr/lib64/build/ax_gcc_func_attribute.m4
/usr/lib64/build/config.guess
/usr/lib64/build/config.sub
/usr/lib64/build/libtool.m4
/usr/lib64/build/ltmain.sh
/usr/lib64/build/mkdep.awk
/usr/lib64/build/phpize.m4
/usr/lib64/build/run-tests.php
/usr/lib64/build/scan_makefile_in.awk
/usr/lib64/build/shtool
/usr/lib64/php/.channels/.alias/pear.txt
/usr/lib64/php/.channels/.alias/pecl.txt
/usr/lib64/php/.channels/.alias/phpdocs.txt
/usr/lib64/php/.channels/__uri.reg
/usr/lib64/php/.channels/doc.php.net.reg
/usr/lib64/php/.channels/pear.php.net.reg
/usr/lib64/php/.channels/pecl.php.net.reg
/usr/lib64/php/.filemap
/usr/lib64/php/.lock
/usr/lib64/php/.registry/archive_tar.reg
/usr/lib64/php/.registry/console_getopt.reg
/usr/lib64/php/.registry/pear.reg
/usr/lib64/php/.registry/structures_graph.reg
/usr/lib64/php/.registry/xml_util.reg
/usr/lib64/php/Archive/Tar.php
/usr/lib64/php/Console/Getopt.php
/usr/lib64/php/OS/Guess.php
/usr/lib64/php/PEAR.php
/usr/lib64/php/PEAR/Builder.php
/usr/lib64/php/PEAR/ChannelFile.php
/usr/lib64/php/PEAR/ChannelFile/Parser.php
/usr/lib64/php/PEAR/Command.php
/usr/lib64/php/PEAR/Command/Auth.php
/usr/lib64/php/PEAR/Command/Auth.xml
/usr/lib64/php/PEAR/Command/Build.php
/usr/lib64/php/PEAR/Command/Build.xml
/usr/lib64/php/PEAR/Command/Channels.php
/usr/lib64/php/PEAR/Command/Channels.xml
/usr/lib64/php/PEAR/Command/Common.php
/usr/lib64/php/PEAR/Command/Config.php
/usr/lib64/php/PEAR/Command/Config.xml
/usr/lib64/php/PEAR/Command/Install.php
/usr/lib64/php/PEAR/Command/Install.xml
/usr/lib64/php/PEAR/Command/Mirror.php
/usr/lib64/php/PEAR/Command/Mirror.xml
/usr/lib64/php/PEAR/Command/Package.php
/usr/lib64/php/PEAR/Command/Package.xml
/usr/lib64/php/PEAR/Command/Pickle.php
/usr/lib64/php/PEAR/Command/Pickle.xml
/usr/lib64/php/PEAR/Command/Registry.php
/usr/lib64/php/PEAR/Command/Registry.xml
/usr/lib64/php/PEAR/Command/Remote.php
/usr/lib64/php/PEAR/Command/Remote.xml
/usr/lib64/php/PEAR/Command/Test.php
/usr/lib64/php/PEAR/Command/Test.xml
/usr/lib64/php/PEAR/Common.php
/usr/lib64/php/PEAR/Config.php
/usr/lib64/php/PEAR/Dependency2.php
/usr/lib64/php/PEAR/DependencyDB.php
/usr/lib64/php/PEAR/Downloader.php
/usr/lib64/php/PEAR/Downloader/Package.php
/usr/lib64/php/PEAR/ErrorStack.php
/usr/lib64/php/PEAR/Exception.php
/usr/lib64/php/PEAR/Frontend.php
/usr/lib64/php/PEAR/Frontend/CLI.php
/usr/lib64/php/PEAR/Installer.php
/usr/lib64/php/PEAR/Installer/Role.php
/usr/lib64/php/PEAR/Installer/Role/Cfg.php
/usr/lib64/php/PEAR/Installer/Role/Cfg.xml
/usr/lib64/php/PEAR/Installer/Role/Common.php
/usr/lib64/php/PEAR/Installer/Role/Data.php
/usr/lib64/php/PEAR/Installer/Role/Data.xml
/usr/lib64/php/PEAR/Installer/Role/Doc.php
/usr/lib64/php/PEAR/Installer/Role/Doc.xml
/usr/lib64/php/PEAR/Installer/Role/Ext.php
/usr/lib64/php/PEAR/Installer/Role/Ext.xml
/usr/lib64/php/PEAR/Installer/Role/Man.php
/usr/lib64/php/PEAR/Installer/Role/Man.xml
/usr/lib64/php/PEAR/Installer/Role/Php.php
/usr/lib64/php/PEAR/Installer/Role/Php.xml
/usr/lib64/php/PEAR/Installer/Role/Script.php
/usr/lib64/php/PEAR/Installer/Role/Script.xml
/usr/lib64/php/PEAR/Installer/Role/Src.php
/usr/lib64/php/PEAR/Installer/Role/Src.xml
/usr/lib64/php/PEAR/Installer/Role/Test.php
/usr/lib64/php/PEAR/Installer/Role/Test.xml
/usr/lib64/php/PEAR/Installer/Role/Www.php
/usr/lib64/php/PEAR/Installer/Role/Www.xml
/usr/lib64/php/PEAR/PackageFile.php
/usr/lib64/php/PEAR/PackageFile/Generator/v1.php
/usr/lib64/php/PEAR/PackageFile/Generator/v2.php
/usr/lib64/php/PEAR/PackageFile/Parser/v1.php
/usr/lib64/php/PEAR/PackageFile/Parser/v2.php
/usr/lib64/php/PEAR/PackageFile/v1.php
/usr/lib64/php/PEAR/PackageFile/v2.php
/usr/lib64/php/PEAR/PackageFile/v2/Validator.php
/usr/lib64/php/PEAR/PackageFile/v2/rw.php
/usr/lib64/php/PEAR/Packager.php
/usr/lib64/php/PEAR/Proxy.php
/usr/lib64/php/PEAR/REST.php
/usr/lib64/php/PEAR/REST/10.php
/usr/lib64/php/PEAR/REST/11.php
/usr/lib64/php/PEAR/REST/13.php
/usr/lib64/php/PEAR/Registry.php
/usr/lib64/php/PEAR/RunTest.php
/usr/lib64/php/PEAR/Task/Common.php
/usr/lib64/php/PEAR/Task/Postinstallscript.php
/usr/lib64/php/PEAR/Task/Postinstallscript/rw.php
/usr/lib64/php/PEAR/Task/Replace.php
/usr/lib64/php/PEAR/Task/Replace/rw.php
/usr/lib64/php/PEAR/Task/Unixeol.php
/usr/lib64/php/PEAR/Task/Unixeol/rw.php
/usr/lib64/php/PEAR/Task/Windowseol.php
/usr/lib64/php/PEAR/Task/Windowseol/rw.php
/usr/lib64/php/PEAR/Validate.php
/usr/lib64/php/PEAR/Validator/PECL.php
/usr/lib64/php/PEAR/XMLParser.php
/usr/lib64/php/Structures/Graph.php
/usr/lib64/php/Structures/Graph/Manipulator/AcyclicTest.php
/usr/lib64/php/Structures/Graph/Manipulator/TopologicalSorter.php
/usr/lib64/php/Structures/Graph/Node.php
/usr/lib64/php/System.php
/usr/lib64/php/XML/Util.php
/usr/lib64/php/data/PEAR/package.dtd
/usr/lib64/php/data/PEAR/template.spec
/usr/lib64/php/doc/Archive_Tar/docs/Archive_Tar.txt
/usr/lib64/php/doc/Structures_Graph/LICENSE
/usr/lib64/php/doc/Structures_Graph/docs/tutorials/Structures_Graph/Structures_Graph.pkg
/usr/lib64/php/doc/XML_Util/examples/example.php
/usr/lib64/php/doc/XML_Util/examples/example2.php
/usr/lib64/php/docs/PEAR/INSTALL
/usr/lib64/php/docs/PEAR/LICENSE
/usr/lib64/php/docs/PEAR/README.rst
/usr/lib64/php/pearcmd.php
/usr/lib64/php/peclcmd.php
/usr/lib64/php/test/Console_Getopt/tests/001-getopt.phpt
/usr/lib64/php/test/Console_Getopt/tests/bug10557.phpt
/usr/lib64/php/test/Console_Getopt/tests/bug11068.phpt
/usr/lib64/php/test/Console_Getopt/tests/bug13140.phpt
/usr/lib64/php/test/Structures_Graph/tests/AcyclicTestTest.php
/usr/lib64/php/test/Structures_Graph/tests/AllTests.php
/usr/lib64/php/test/Structures_Graph/tests/BasicGraphTest.php
/usr/lib64/php/test/Structures_Graph/tests/TopologicalSorterTest.php
/usr/lib64/php/test/Structures_Graph/tests/helper.inc
/usr/lib64/php/test/XML_Util/tests/AbstractUnitTests.php
/usr/lib64/php/test/XML_Util/tests/ApiVersionTests.php
/usr/lib64/php/test/XML_Util/tests/AttributesToStringTests.php
/usr/lib64/php/test/XML_Util/tests/Bug18343Tests.php
/usr/lib64/php/test/XML_Util/tests/Bug21177Tests.php
/usr/lib64/php/test/XML_Util/tests/Bug21184Tests.php
/usr/lib64/php/test/XML_Util/tests/Bug4950Tests.php
/usr/lib64/php/test/XML_Util/tests/Bug5392Tests.php
/usr/lib64/php/test/XML_Util/tests/CollapseEmptyTagsTests.php
/usr/lib64/php/test/XML_Util/tests/CreateCDataSectionTests.php
/usr/lib64/php/test/XML_Util/tests/CreateCommentTests.php
/usr/lib64/php/test/XML_Util/tests/CreateEndElementTests.php
/usr/lib64/php/test/XML_Util/tests/CreateStartElementTests.php
/usr/lib64/php/test/XML_Util/tests/CreateTagFromArrayTests.php
/usr/lib64/php/test/XML_Util/tests/CreateTagTests.php
/usr/lib64/php/test/XML_Util/tests/GetDocTypeDeclarationTests.php
/usr/lib64/php/test/XML_Util/tests/GetXmlDeclarationTests.php
/usr/lib64/php/test/XML_Util/tests/IsValidNameTests.php
/usr/lib64/php/test/XML_Util/tests/RaiseErrorTests.php
/usr/lib64/php/test/XML_Util/tests/ReplaceEntitiesTests.php
/usr/lib64/php/test/XML_Util/tests/ReverseEntitiesTests.php
/usr/lib64/php/test/XML_Util/tests/SplitQualifiedNameTests.php

%files bin
%defattr(-,root,root,-)
/usr/bin/pear
/usr/bin/peardev
/usr/bin/pecl
/usr/bin/phar
/usr/bin/phar.phar
/usr/bin/php
/usr/bin/php-cgi
/usr/bin/php-config
/usr/bin/php-fpm
/usr/bin/phpdbg
/usr/bin/phpize

%files data
%defattr(-,root,root,-)
/usr/share/clr-service-restart/php-fpm.service
/usr/share/defaults/httpd/conf.d/php.conf
/usr/share/defaults/php/pear.conf
/usr/share/defaults/php/php-fpm.conf
/usr/share/defaults/php/php-fpm.d/www.conf
/usr/share/defaults/php/php.ini
/usr/share/fpm/status.html

%files dev
%defattr(-,root,root,-)
/usr/include/php/TSRM/TSRM.h
/usr/include/php/TSRM/readdir.h
/usr/include/php/TSRM/tsrm_config.h
/usr/include/php/TSRM/tsrm_config.w32.h
/usr/include/php/TSRM/tsrm_config_common.h
/usr/include/php/TSRM/tsrm_strtok_r.h
/usr/include/php/TSRM/tsrm_win32.h
/usr/include/php/Zend/zend.h
/usr/include/php/Zend/zend_API.h
/usr/include/php/Zend/zend_alloc.h
/usr/include/php/Zend/zend_alloc_sizes.h
/usr/include/php/Zend/zend_arena.h
/usr/include/php/Zend/zend_ast.h
/usr/include/php/Zend/zend_bitset.h
/usr/include/php/Zend/zend_build.h
/usr/include/php/Zend/zend_builtin_functions.h
/usr/include/php/Zend/zend_closures.h
/usr/include/php/Zend/zend_compile.h
/usr/include/php/Zend/zend_config.h
/usr/include/php/Zend/zend_config.nw.h
/usr/include/php/Zend/zend_config.w32.h
/usr/include/php/Zend/zend_constants.h
/usr/include/php/Zend/zend_cpuinfo.h
/usr/include/php/Zend/zend_dtrace.h
/usr/include/php/Zend/zend_errors.h
/usr/include/php/Zend/zend_exceptions.h
/usr/include/php/Zend/zend_execute.h
/usr/include/php/Zend/zend_extensions.h
/usr/include/php/Zend/zend_float.h
/usr/include/php/Zend/zend_gc.h
/usr/include/php/Zend/zend_generators.h
/usr/include/php/Zend/zend_globals.h
/usr/include/php/Zend/zend_globals_macros.h
/usr/include/php/Zend/zend_hash.h
/usr/include/php/Zend/zend_highlight.h
/usr/include/php/Zend/zend_inheritance.h
/usr/include/php/Zend/zend_ini.h
/usr/include/php/Zend/zend_ini_parser.h
/usr/include/php/Zend/zend_ini_scanner.h
/usr/include/php/Zend/zend_ini_scanner_defs.h
/usr/include/php/Zend/zend_interfaces.h
/usr/include/php/Zend/zend_istdiostream.h
/usr/include/php/Zend/zend_iterators.h
/usr/include/php/Zend/zend_language_parser.h
/usr/include/php/Zend/zend_language_scanner.h
/usr/include/php/Zend/zend_language_scanner_defs.h
/usr/include/php/Zend/zend_list.h
/usr/include/php/Zend/zend_llist.h
/usr/include/php/Zend/zend_long.h
/usr/include/php/Zend/zend_modules.h
/usr/include/php/Zend/zend_multibyte.h
/usr/include/php/Zend/zend_multiply.h
/usr/include/php/Zend/zend_object_handlers.h
/usr/include/php/Zend/zend_objects.h
/usr/include/php/Zend/zend_objects_API.h
/usr/include/php/Zend/zend_operators.h
/usr/include/php/Zend/zend_portability.h
/usr/include/php/Zend/zend_ptr_stack.h
/usr/include/php/Zend/zend_range_check.h
/usr/include/php/Zend/zend_signal.h
/usr/include/php/Zend/zend_smart_str.h
/usr/include/php/Zend/zend_smart_str_public.h
/usr/include/php/Zend/zend_smart_string.h
/usr/include/php/Zend/zend_smart_string_public.h
/usr/include/php/Zend/zend_sort.h
/usr/include/php/Zend/zend_stack.h
/usr/include/php/Zend/zend_stream.h
/usr/include/php/Zend/zend_string.h
/usr/include/php/Zend/zend_strtod.h
/usr/include/php/Zend/zend_strtod_int.h
/usr/include/php/Zend/zend_ts_hash.h
/usr/include/php/Zend/zend_type_info.h
/usr/include/php/Zend/zend_types.h
/usr/include/php/Zend/zend_variables.h
/usr/include/php/Zend/zend_virtual_cwd.h
/usr/include/php/Zend/zend_vm.h
/usr/include/php/Zend/zend_vm_def.h
/usr/include/php/Zend/zend_vm_execute.h
/usr/include/php/Zend/zend_vm_handlers.h
/usr/include/php/Zend/zend_vm_opcodes.h
/usr/include/php/Zend/zend_vm_trace_handlers.h
/usr/include/php/Zend/zend_vm_trace_map.h
/usr/include/php/ext/date/lib/timelib.h
/usr/include/php/ext/date/lib/timelib_config.h
/usr/include/php/ext/date/php_date.h
/usr/include/php/ext/dom/xml_common.h
/usr/include/php/ext/filter/php_filter.h
/usr/include/php/ext/gd/gd_compat.h
/usr/include/php/ext/gd/libgd/bmp.h
/usr/include/php/ext/gd/libgd/gd.h
/usr/include/php/ext/gd/libgd/gd_errors.h
/usr/include/php/ext/gd/libgd/gd_intern.h
/usr/include/php/ext/gd/libgd/gd_io.h
/usr/include/php/ext/gd/libgd/gdcache.h
/usr/include/php/ext/gd/libgd/gdfontg.h
/usr/include/php/ext/gd/libgd/gdfontl.h
/usr/include/php/ext/gd/libgd/gdfontmb.h
/usr/include/php/ext/gd/libgd/gdfonts.h
/usr/include/php/ext/gd/libgd/gdfontt.h
/usr/include/php/ext/gd/libgd/gdhelpers.h
/usr/include/php/ext/gd/libgd/jisx0208.h
/usr/include/php/ext/gd/libgd/wbmp.h
/usr/include/php/ext/gd/php_gd.h
/usr/include/php/ext/gmp/php_gmp_int.h
/usr/include/php/ext/hash/php_hash.h
/usr/include/php/ext/hash/php_hash_adler32.h
/usr/include/php/ext/hash/php_hash_crc32.h
/usr/include/php/ext/hash/php_hash_fnv.h
/usr/include/php/ext/hash/php_hash_gost.h
/usr/include/php/ext/hash/php_hash_haval.h
/usr/include/php/ext/hash/php_hash_joaat.h
/usr/include/php/ext/hash/php_hash_md.h
/usr/include/php/ext/hash/php_hash_ripemd.h
/usr/include/php/ext/hash/php_hash_sha.h
/usr/include/php/ext/hash/php_hash_sha3.h
/usr/include/php/ext/hash/php_hash_snefru.h
/usr/include/php/ext/hash/php_hash_tiger.h
/usr/include/php/ext/hash/php_hash_whirlpool.h
/usr/include/php/ext/iconv/php_have_bsd_iconv.h
/usr/include/php/ext/iconv/php_have_glibc_iconv.h
/usr/include/php/ext/iconv/php_have_ibm_iconv.h
/usr/include/php/ext/iconv/php_have_iconv.h
/usr/include/php/ext/iconv/php_have_libiconv.h
/usr/include/php/ext/iconv/php_iconv.h
/usr/include/php/ext/iconv/php_iconv_aliased_libiconv.h
/usr/include/php/ext/iconv/php_iconv_broken_ignore.h
/usr/include/php/ext/iconv/php_iconv_supports_errno.h
/usr/include/php/ext/iconv/php_php_iconv_h_path.h
/usr/include/php/ext/iconv/php_php_iconv_impl.h
/usr/include/php/ext/json/php_json.h
/usr/include/php/ext/json/php_json_parser.h
/usr/include/php/ext/json/php_json_scanner.h
/usr/include/php/ext/libxml/php_libxml.h
/usr/include/php/ext/mbstring/libmbfl/config.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/eaw_table.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfilter.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfilter_8bit.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfilter_pass.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfilter_wchar.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_allocators.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_consts.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_convert.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_defs.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_encoding.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_filter_output.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_ident.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_language.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_memory_device.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_string.h
/usr/include/php/ext/mbstring/mbstring.h
/usr/include/php/ext/mbstring/php_mbregex.h
/usr/include/php/ext/mbstring/php_onig_compat.h
/usr/include/php/ext/mysqli/mysqli_mysqlnd.h
/usr/include/php/ext/mysqli/php_mysqli_structs.h
/usr/include/php/ext/mysqlnd/config-win.h
/usr/include/php/ext/mysqlnd/mysql_float_to_double.h
/usr/include/php/ext/mysqlnd/mysqlnd.h
/usr/include/php/ext/mysqlnd/mysqlnd_alloc.h
/usr/include/php/ext/mysqlnd/mysqlnd_auth.h
/usr/include/php/ext/mysqlnd/mysqlnd_block_alloc.h
/usr/include/php/ext/mysqlnd/mysqlnd_charset.h
/usr/include/php/ext/mysqlnd/mysqlnd_commands.h
/usr/include/php/ext/mysqlnd/mysqlnd_connection.h
/usr/include/php/ext/mysqlnd/mysqlnd_debug.h
/usr/include/php/ext/mysqlnd/mysqlnd_enum_n_def.h
/usr/include/php/ext/mysqlnd/mysqlnd_ext_plugin.h
/usr/include/php/ext/mysqlnd/mysqlnd_libmysql_compat.h
/usr/include/php/ext/mysqlnd/mysqlnd_plugin.h
/usr/include/php/ext/mysqlnd/mysqlnd_portability.h
/usr/include/php/ext/mysqlnd/mysqlnd_priv.h
/usr/include/php/ext/mysqlnd/mysqlnd_protocol_frame_codec.h
/usr/include/php/ext/mysqlnd/mysqlnd_ps.h
/usr/include/php/ext/mysqlnd/mysqlnd_read_buffer.h
/usr/include/php/ext/mysqlnd/mysqlnd_result.h
/usr/include/php/ext/mysqlnd/mysqlnd_result_meta.h
/usr/include/php/ext/mysqlnd/mysqlnd_reverse_api.h
/usr/include/php/ext/mysqlnd/mysqlnd_statistics.h
/usr/include/php/ext/mysqlnd/mysqlnd_structs.h
/usr/include/php/ext/mysqlnd/mysqlnd_vio.h
/usr/include/php/ext/mysqlnd/mysqlnd_wireprotocol.h
/usr/include/php/ext/mysqlnd/php_mysqlnd.h
/usr/include/php/ext/pcre/pcre2lib/config.h
/usr/include/php/ext/pcre/pcre2lib/pcre2.h
/usr/include/php/ext/pcre/pcre2lib/pcre2_internal.h
/usr/include/php/ext/pcre/pcre2lib/pcre2_intmodedep.h
/usr/include/php/ext/pcre/pcre2lib/pcre2_ucp.h
/usr/include/php/ext/pcre/php_pcre.h
/usr/include/php/ext/pdo/php_pdo.h
/usr/include/php/ext/pdo/php_pdo_driver.h
/usr/include/php/ext/pdo/php_pdo_error.h
/usr/include/php/ext/phar/php_phar.h
/usr/include/php/ext/session/mod_files.h
/usr/include/php/ext/session/mod_user.h
/usr/include/php/ext/session/php_session.h
/usr/include/php/ext/simplexml/php_simplexml.h
/usr/include/php/ext/simplexml/php_simplexml_exports.h
/usr/include/php/ext/sockets/php_sockets.h
/usr/include/php/ext/spl/php_spl.h
/usr/include/php/ext/spl/spl_array.h
/usr/include/php/ext/spl/spl_directory.h
/usr/include/php/ext/spl/spl_dllist.h
/usr/include/php/ext/spl/spl_engine.h
/usr/include/php/ext/spl/spl_exceptions.h
/usr/include/php/ext/spl/spl_fixedarray.h
/usr/include/php/ext/spl/spl_functions.h
/usr/include/php/ext/spl/spl_heap.h
/usr/include/php/ext/spl/spl_iterators.h
/usr/include/php/ext/spl/spl_observer.h
/usr/include/php/ext/sqlite3/libsqlite/sqlite3.h
/usr/include/php/ext/standard/base64.h
/usr/include/php/ext/standard/basic_functions.h
/usr/include/php/ext/standard/crc32.h
/usr/include/php/ext/standard/credits.h
/usr/include/php/ext/standard/credits_ext.h
/usr/include/php/ext/standard/credits_sapi.h
/usr/include/php/ext/standard/crypt_blowfish.h
/usr/include/php/ext/standard/crypt_freesec.h
/usr/include/php/ext/standard/css.h
/usr/include/php/ext/standard/cyr_convert.h
/usr/include/php/ext/standard/datetime.h
/usr/include/php/ext/standard/dl.h
/usr/include/php/ext/standard/exec.h
/usr/include/php/ext/standard/file.h
/usr/include/php/ext/standard/flock_compat.h
/usr/include/php/ext/standard/fsock.h
/usr/include/php/ext/standard/head.h
/usr/include/php/ext/standard/hrtime.h
/usr/include/php/ext/standard/html.h
/usr/include/php/ext/standard/html_tables.h
/usr/include/php/ext/standard/info.h
/usr/include/php/ext/standard/md5.h
/usr/include/php/ext/standard/microtime.h
/usr/include/php/ext/standard/pack.h
/usr/include/php/ext/standard/pageinfo.h
/usr/include/php/ext/standard/php_array.h
/usr/include/php/ext/standard/php_assert.h
/usr/include/php/ext/standard/php_browscap.h
/usr/include/php/ext/standard/php_crypt.h
/usr/include/php/ext/standard/php_crypt_r.h
/usr/include/php/ext/standard/php_dir.h
/usr/include/php/ext/standard/php_dns.h
/usr/include/php/ext/standard/php_ext_syslog.h
/usr/include/php/ext/standard/php_filestat.h
/usr/include/php/ext/standard/php_fopen_wrappers.h
/usr/include/php/ext/standard/php_ftok.h
/usr/include/php/ext/standard/php_http.h
/usr/include/php/ext/standard/php_image.h
/usr/include/php/ext/standard/php_incomplete_class.h
/usr/include/php/ext/standard/php_iptc.h
/usr/include/php/ext/standard/php_lcg.h
/usr/include/php/ext/standard/php_link.h
/usr/include/php/ext/standard/php_mail.h
/usr/include/php/ext/standard/php_math.h
/usr/include/php/ext/standard/php_metaphone.h
/usr/include/php/ext/standard/php_mt_rand.h
/usr/include/php/ext/standard/php_net.h
/usr/include/php/ext/standard/php_password.h
/usr/include/php/ext/standard/php_rand.h
/usr/include/php/ext/standard/php_random.h
/usr/include/php/ext/standard/php_smart_string.h
/usr/include/php/ext/standard/php_smart_string_public.h
/usr/include/php/ext/standard/php_standard.h
/usr/include/php/ext/standard/php_string.h
/usr/include/php/ext/standard/php_type.h
/usr/include/php/ext/standard/php_uuencode.h
/usr/include/php/ext/standard/php_var.h
/usr/include/php/ext/standard/php_versioning.h
/usr/include/php/ext/standard/proc_open.h
/usr/include/php/ext/standard/quot_print.h
/usr/include/php/ext/standard/scanf.h
/usr/include/php/ext/standard/sha1.h
/usr/include/php/ext/standard/streamsfuncs.h
/usr/include/php/ext/standard/uniqid.h
/usr/include/php/ext/standard/url.h
/usr/include/php/ext/standard/url_scanner_ex.h
/usr/include/php/ext/standard/winver.h
/usr/include/php/ext/xml/expat_compat.h
/usr/include/php/ext/xml/php_xml.h
/usr/include/php/main/SAPI.h
/usr/include/php/main/build-defs.h
/usr/include/php/main/fastcgi.h
/usr/include/php/main/fopen_wrappers.h
/usr/include/php/main/http_status_codes.h
/usr/include/php/main/php.h
/usr/include/php/main/php_compat.h
/usr/include/php/main/php_config.h
/usr/include/php/main/php_content_types.h
/usr/include/php/main/php_getopt.h
/usr/include/php/main/php_globals.h
/usr/include/php/main/php_ini.h
/usr/include/php/main/php_main.h
/usr/include/php/main/php_memory_streams.h
/usr/include/php/main/php_network.h
/usr/include/php/main/php_open_temporary_file.h
/usr/include/php/main/php_output.h
/usr/include/php/main/php_reentrancy.h
/usr/include/php/main/php_scandir.h
/usr/include/php/main/php_stdint.h
/usr/include/php/main/php_streams.h
/usr/include/php/main/php_syslog.h
/usr/include/php/main/php_ticks.h
/usr/include/php/main/php_variables.h
/usr/include/php/main/php_version.h
/usr/include/php/main/rfc1867.h
/usr/include/php/main/snprintf.h
/usr/include/php/main/spprintf.h
/usr/include/php/main/streams/php_stream_context.h
/usr/include/php/main/streams/php_stream_filter_api.h
/usr/include/php/main/streams/php_stream_glob_wrapper.h
/usr/include/php/main/streams/php_stream_mmap.h
/usr/include/php/main/streams/php_stream_plain_wrapper.h
/usr/include/php/main/streams/php_stream_transport.h
/usr/include/php/main/streams/php_stream_userspace.h
/usr/include/php/main/streams/php_streams_int.h
/usr/include/php/sapi/cli/cli.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20180731/dba.so
/usr/lib64/extensions/no-debug-non-zts-20180731/opcache.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php/TSRM_LICENSE
/usr/share/package-licenses/php/Zend_LICENSE
/usr/share/package-licenses/php/ext_bcmath_libbcmath_COPYING.LIB
/usr/share/package-licenses/php/ext_date_lib_LICENSE.rst
/usr/share/package-licenses/php/ext_fileinfo_libmagic_LICENSE
/usr/share/package-licenses/php/ext_mbstring_libmbfl_LICENSE
/usr/share/package-licenses/php/ext_mbstring_oniguruma_COPYING
/usr/share/package-licenses/php/ext_mbstring_ucgendat_OPENLDAP_LICENSE
/usr/share/package-licenses/php/ext_zip_LICENSE_libzip
/usr/share/package-licenses/php/sapi_fpm_LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/phar.1
/usr/share/man/man1/phar.phar.1
/usr/share/man/man1/php-cgi.1
/usr/share/man/man1/php-config.1
/usr/share/man/man1/php.1
/usr/share/man/man1/phpdbg.1
/usr/share/man/man1/phpize.1
/usr/share/man/man8/php-fpm.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/php-fpm.service
