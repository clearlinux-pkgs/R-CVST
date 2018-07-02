#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-CVST
Version  : 0.2.2
Release  : 12
URL      : https://cran.r-project.org/src/contrib/CVST_0.2-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/CVST_0.2-2.tar.gz
Summary  : Fast Cross-Validation via Sequential Testing
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-kernlab
BuildRequires : R-kernlab
BuildRequires : clr-R-helpers

%description
CVST
====
Fast Cross-Validation via Sequential Testing
The package CVST is hosted on CRAN, so

%prep
%setup -q -c -n CVST

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1527428041

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1527428041
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library CVST
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library CVST
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library CVST
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library CVST|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/CVST/DESCRIPTION
/usr/lib64/R/library/CVST/INDEX
/usr/lib64/R/library/CVST/Meta/Rd.rds
/usr/lib64/R/library/CVST/Meta/features.rds
/usr/lib64/R/library/CVST/Meta/hsearch.rds
/usr/lib64/R/library/CVST/Meta/links.rds
/usr/lib64/R/library/CVST/Meta/nsInfo.rds
/usr/lib64/R/library/CVST/Meta/package.rds
/usr/lib64/R/library/CVST/NAMESPACE
/usr/lib64/R/library/CVST/R/CVST
/usr/lib64/R/library/CVST/R/CVST.rdb
/usr/lib64/R/library/CVST/R/CVST.rdx
/usr/lib64/R/library/CVST/help/AnIndex
/usr/lib64/R/library/CVST/help/CVST.rdb
/usr/lib64/R/library/CVST/help/CVST.rdx
/usr/lib64/R/library/CVST/help/aliases.rds
/usr/lib64/R/library/CVST/help/paths.rds
/usr/lib64/R/library/CVST/html/00Index.html
/usr/lib64/R/library/CVST/html/R.css
