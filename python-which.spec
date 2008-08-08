Name:           python-which
Version:        1.1.0
Release:        %mkrel 2
Summary:        Small which replacement that can be used as a Python module

Group:          Development/Python
License:        MIT
URL:            http://trentm.com/projects/which/
Source0:        http://trentm.com/downloads/which/%{version}/which-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
%py_requires -d

%description
which.py is a small which replacement. It has the following features:

 * it can print all matches on the PATH;
 * it can note "near misses" on the PATH (e.g. files that match but 
   may not, say, have execute permissions); and
 * it can be used as a Python module.


%prep
%setup -q -n which-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
# add a script that calls the python module
cat << \EOF > which-python
#!/bin/sh
python -m which $@
EOF
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m0755 -p which-python $RPM_BUILD_ROOT%{_bindir}

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.txt TODO.txt
%{_bindir}/which-python
%{python_sitelib}/which.py*
%{python_sitelib}/which-*.egg-info


