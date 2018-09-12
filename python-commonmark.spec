# TODO:
# - package %{_bindir}/cmark
#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python parser for the CommonMark Markdown spec
Name:		python-commonmark
Version:	0.7.5
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/c/commonmark/CommonMark-%{version}.tar.gz
# Source0-md5:	70cb4ade4b9d0370213be9816f99a21e
URL:		https://github.com/rtfd/CommonMark-py
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CommonMark-py is a pure Python port of jgm’s commonmark.js, a Markdown
parser and renderer for the CommonMark specification, using only
native modules.

%package -n python3-commonmark
Summary:	Python parser for the CommonMark Markdown spec
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-commonmark
CommonMark-py is a pure Python port of jgm’s commonmark.js, a Markdown
parser and renderer for the CommonMark specification, using only
native modules.

%prep
%setup -q -n CommonMark-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/CommonMark
%{py_sitescriptdir}/CommonMark-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-commonmark
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/CommonMark
%{py3_sitescriptdir}/CommonMark-%{version}-py*.egg-info
%endif
