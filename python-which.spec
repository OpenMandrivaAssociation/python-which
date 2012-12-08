Name:           python-which
Version:        1.1.0
Release:        %mkrel 7
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




%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-7mdv2011.0
+ Revision: 668050
- mass rebuild

* Fri Oct 29 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.1.0-6mdv2011.0
+ Revision: 589984
- rebuild for python-2.7

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-5mdv2010.1
+ Revision: 524111
- rebuilt for 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0-4mdv2010.0
+ Revision: 442543
- rebuild

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 1.1.0-3mdv2009.1
+ Revision: 323410
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0-2mdv2009.0
+ Revision: 269044
- rebuild early 2009.0 package (before pixel changes)

  + David Walluck <walluck@mandriva.org>
    - import python-which


* Mon Jan  7 2008 Patrice Dumas <pertusus@free.fr> - 1.1.0-3
- ship egg file

* Sun Oct 28 2007  <ndbecker2@gmail.com> - 1.1.0-2
- Remove ref to GNU

* Sat Oct 27 2007  <ndbecker2@gmail.com> - 1.1.0-1
- Package for fedora

* Thu Jul 19 2007 Patrice Dumas <pertusus@free.fr> 1.1.0-1
- initial packaging
