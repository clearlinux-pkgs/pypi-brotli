#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-brotli
Version  : 1.0.9
Release  : 7
URL      : https://files.pythonhosted.org/packages/2a/18/70c32fe9357f3eea18598b23aa9ed29b1711c3001835f7cf99a9818985d0/Brotli-1.0.9.zip
Source0  : https://files.pythonhosted.org/packages/2a/18/70c32fe9357f3eea18598b23aa9ed29b1711c3001835f7cf99a9818985d0/Brotli-1.0.9.zip
Summary  : Python bindings for the Brotli compression library
Group    : Development/Tools
License  : MIT
Requires: pypi-brotli-filemap = %{version}-%{release}
Requires: pypi-brotli-lib = %{version}-%{release}
Requires: pypi-brotli-license = %{version}-%{release}
Requires: pypi-brotli-python = %{version}-%{release}
Requires: pypi-brotli-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
BROTLI DATA COMPRESSION LIBRARY
Brotli is a generic-purpose lossless compression algorithm that compresses data
using a combination of a modern variant of the LZ77 algorithm, Huffman coding
and 2nd order context modeling, with a compression ratio comparable to the best
currently available general-purpose compression methods. It is similar in speed
with deflate but offers more dense compression.

%package filemap
Summary: filemap components for the pypi-brotli package.
Group: Default

%description filemap
filemap components for the pypi-brotli package.


%package lib
Summary: lib components for the pypi-brotli package.
Group: Libraries
Requires: pypi-brotli-license = %{version}-%{release}
Requires: pypi-brotli-filemap = %{version}-%{release}

%description lib
lib components for the pypi-brotli package.


%package license
Summary: license components for the pypi-brotli package.
Group: Default

%description license
license components for the pypi-brotli package.


%package python
Summary: python components for the pypi-brotli package.
Group: Default
Requires: pypi-brotli-python3 = %{version}-%{release}

%description python
python components for the pypi-brotli package.


%package python3
Summary: python3 components for the pypi-brotli package.
Group: Default
Requires: pypi-brotli-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(brotli)

%description python3
python3 components for the pypi-brotli package.


%prep
%setup -q -n Brotli-1.0.9
cd %{_builddir}/Brotli-1.0.9
pushd ..
cp -a Brotli-1.0.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656362435
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-brotli
cp %{_builddir}/Brotli-1.0.9/LICENSE %{buildroot}/usr/share/package-licenses/pypi-brotli/c045813a6c514f2d30d60a07c6aaf3603850e608
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-brotli

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-brotli/c045813a6c514f2d30d60a07c6aaf3603850e608

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
