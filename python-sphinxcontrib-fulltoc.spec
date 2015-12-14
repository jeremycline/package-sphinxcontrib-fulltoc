%global srcname sphinxcontrib-fulltoc
%global sum Include a full table of contents in your Sphinx HTML sidebar


Name: python-%{srcname}
Version: 1.1
Release: 1%{?dist}
Summary: %{sum}	
License: ASL 2.0
URL: https://github.com/dreamhost/%{srcname}
Source0: https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch: noarch


%description
sphinxcontrib-fulltoc is an extension for the Sphinx documentation system that
changes the HTML output to include a more detailed table of contents in the
sidebar. By default Sphinx only shows the local headers for the current page.
With the extension installed, all of the page titles are included, and the
local headers for the current page are also included in the appropriate place
within the document.


%package -n python2-%{srcname}
Summary: %{sum}
BuildRequires: python2-devel
BuildRequires: python-pbr
Requires: python-sphinx
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
sphinxcontrib-fulltoc is an extension for the Sphinx documentation system that
changes the HTML output to include a more detailed table of contents in the
sidebar. By default Sphinx only shows the local headers for the current page.
With the extension installed, all of the page titles are included, and the
local headers for the current page are also included in the appropriate place
within the document.


%package -n python3-%{srcname}
Summary: %{sum}
BuildRequires: python3-devel
BuildRequires: python3-pbr
Requires: python3-sphinx
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
sphinxcontrib-fulltoc is an extension for the Sphinx documentation system that
changes the HTML output to include a more detailed table of contents in the
sidebar. By default Sphinx only shows the local headers for the current page.
With the extension installed, all of the page titles are included, and the
local headers for the current page are also included in the appropriate place
within the document.


%prep
%autosetup -n %{srcname}-%{version}
rm -r *.egg-info
find . -name '*.py[co]' -delete


%build
%py2_build
%py3_build


%install
%py2_install
%py3_install


%files -n python2-%{srcname}
%license LICENSE
%doc README.rst AUTHORS ChangeLog announce.rst
%{python2_sitelib}/*


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst AUTHORS ChangeLog announce.rst
%{python3_sitelib}/*


%changelog
* Sat Dec 12 2015 Jeremy Cline <jeremy@jcline.org> 1.1-1
- Initial release
