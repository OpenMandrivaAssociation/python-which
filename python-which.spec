%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary:	Small which replacement that can be used as a Python module
Name:		python-which
Version:	1.1.0
Release:	14
Group:		Development/Python
License:	MIT
Url:		http://trentm.com/projects/which/
Source0:	http://trentm.com/downloads/which/%{version}/which-%{version}.zip
BuildArch:	noarch
BuildRequires:  python-devel

%description
which.py is a small which replacement. It has the following features:

 * it can print all matches on the PATH;
 * it can note "near misses" on the PATH (e.g. files that match but 
   may not, say, have execute permissions); and
 * it can be used as a Python module.

%prep
%setup -qn which-%{version}


%build
python setup.py build


%install
python setup.py install -O1 --skip-build --root %{buildroot}
# add a script that calls the python module
cat << \EOF > which-python
#!/bin/sh
python -m which $@
EOF
mkdir -p %{buildroot}%{_bindir}
install -m0755 -p which-python %{buildroot}%{_bindir}

%files
%doc LICENSE.txt README.txt TODO.txt
%{_bindir}/which-python
%{python_sitelib}/which.py*
%{python_sitelib}/which-*.egg-info

