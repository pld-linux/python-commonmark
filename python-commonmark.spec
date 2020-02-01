#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
%bcond_without	tests	# unit tests

Summary:	Python parser for the CommonMark Markdown spec
Summary(pl.UTF-8):	Pythonowy parser specyfikacji CommonMark Markdown
Name:		python-commonmark
Version:	0.9.1
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/commonmark/
Source0:	https://files.pythonhosted.org/packages/source/c/commonmark/commonmark-%{version}.tar.gz
# Source0-md5:	cd1dc70c4714d9ed4117a40490c25e00
Patch0:		%{name}-deps.patch
URL:		https://github.com/rtfd/CommonMark-py
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-future >= 0.14.0
BuildRequires:	python-hypothesis >= 3.55.3
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-hypothesis >= 3.55.3
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-future
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CommonMark-py is a pure Python port of jgm's commonmark.js, a Markdown
parser and renderer for the CommonMark specification, using only
native modules.

%description -l pl.UTF-8
CommonMark-py to czysto perlowy port kodu jgm commonmark.js - parsera
i renderera specyfikacji CommonMark, napisany przy wyłącznie przy
użyciu natywnych modułów.

%package -n python3-commonmark
Summary:	Python parser for the CommonMark Markdown spec
Summary(pl.UTF-8):	Pythonowy parser specyfikacji CommonMark Markdown
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-commonmark
CommonMark-py is a pure Python port of jgm's commonmark.js, a Markdown
parser and renderer for the CommonMark specification, using only
native modules.

%description -n python3-commonmark -l pl.UTF-8
CommonMark-py to czysto perlowy port kodu jgm commonmark.js - parsera
i renderera specyfikacji CommonMark, napisany przy wyłącznie przy
użyciu natywnych modułów.

%prep
%setup -q -n commonmark-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
LC_ALL=C.UTF-8 \
PYTHONIOENCODING=utf-8 \
PYTHONPATH=$(pwd)/build-2/lib \
%{__python} commonmark/tests/run_spec_tests.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
LC_ALL=C.UTF-8 \
PYTHONPATH=$(pwd)/build-3/lib \
%{__python3} commonmark/tests/run_spec_tests.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/cmark{,-2}
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/cmark{,-3}

ln -sf cmark-3 $RPM_BUILD_ROOT%{_bindir}/cmark
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.rst spec.txt
%attr(755,root,root) %{_bindir}/cmark-2
%{py_sitescriptdir}/commonmark
%{py_sitescriptdir}/commonmark-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-commonmark
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.rst spec.txt
%attr(755,root,root) %{_bindir}/cmark
%attr(755,root,root) %{_bindir}/cmark-3
%{py3_sitescriptdir}/commonmark
%{py3_sitescriptdir}/commonmark-%{version}-py*.egg-info
%endif
