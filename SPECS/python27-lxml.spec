%global pymajor 2
%global pyminor 7
%global pyver %{pymajor}.%{pyminor}
%global iusver %{pymajor}%{pyminor}
%global __python2 %{_bindir}/python%{pyver}
%global python2_sitelib  %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")
%global __os_install_post %{__python27_os_install_post}
%global srcname lxml
%global src %(echo %{srcname} | cut -c1)

Name:           python%{iusver}-%{srcname}
Version:        3.4.1
Release:        1.ius%{?dist}
Summary:        ElementTree-like Python bindings for libxml2 and libxslt
Vendor:         IUS Community Project
Group:          Development/Libraries
License:        BSD
URL:            http://lxml.de/
Source0:        https://pypi.python.org/packages/source/%{src}/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libxslt-devel
BuildRequires:  python%{iusver}-devel
BuildRequires:  python%{iusver}-setuptools


%description
lxml provides a Python binding to the libxslt and libxml2 libraries.
It follows the ElementTree API as much as possible in order to provide
a more Pythonic interface to libxml2 and libxslt than the default
bindings.  In particular, lxml deals with Python Unicode strings
rather than encoded UTF-8 and handles memory management automatically,
unlike the default bindings.


%prep
%setup -q -n %{srcname}-%{version}
find -name '*.py' -type f -print0 | xargs -0 sed -i '1s|python|&%{pyver}|'
chmod a-x doc/rest2html.py


%build
CFLAGS=$RPM_OPT_FLAGS %{__python2} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python2} setup.py install --optimize 1 --skip-build --root %{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSES.txt PKG-INFO CREDITS.txt CHANGES.txt doc/
%{python2_sitearch}/*


%changelog
* Fri Nov 21 2014 Ben Harper <ben.harper@rackspace.com> - 3.4.1-1.ius
- Latest sources from upstream

* Thu Sep 11 2014 Ben Harper <ben.harper@rackspace.com> - 3.4.0-1.ius
- Latest sources from upstream

* Fri Aug 29 2014 Carl George <carl.george@rackspace.com> - 3.3.6-1.ius
- Latest sources from upstream

* Fri Jun 06 2014 Carl George <carl.george@rackspace.com> - 3.3.5-2.ius
- Update upstream url
- Override __os_install_post to fix .pyc/pyo magic
- Implement python packaging best practices

* Fri Apr 18 2014 Ben Harper <ben.harper@rackspace.com> - 3.3.5-1.ius
- Latest sources from upstream

* Fri Apr 04 2014 Ben Harper <ben.harper@rackspace.com> - 3.3.4-1.ius
- Latest sources from upstream

* Wed Mar 05 2014 Ben Harper <ben.harper@rackspace.com> - 3.3.3-1.ius
- Latest sources from upstream

* Mon Mar 03 2014 Ben Harper <ben.harper@rackspace.com> - 3.3.2-1.ius
- Latest sources from upstream

* Wed Feb 12 2014 Ben Harper <ben.harper@rackspace.com> - 3.3.1-1.ius
- Latest sources from upstream

* Mon Jan 27 2014 Ben Harper <ben.harper@rackspace.com> - 3.3.0-1.ius
- Latest sources from upstream

* Fri Jan 03 2014 Ben Harper <ben.harper@rackspace.com> - 3.2.5-1.ius
- Latest sources from upstream

* Mon Nov 11 2013 Ben Harper <ben.harper@rackspace.com> - 3.2.4-1.ius
- Latest sources from upstream

* Mon Jul 29 2013 Ben Harper <ben.harper@rackspace.com> - 3.2.3-1.ius
- Latest sources from upstream

* Mon May 13 2013 Ben Harper <ben.harper@rackspace.com> - 3.2.1-1.ius
- Building latest 3.2.1

* Mon Apr 29 2013 Ben Harper <ben.harper@rackspace.com> - 3.2.0-1.ius
- Building latest 3.2.0

* Fri Apr 12 2013 Ben Harper <ben.harper@rackspace.com> - 3.1.2-1.ius
- Building latest 3.1.2

* Wed Apr 10 2013 Jeffrey Ness <jeffrey.ness@racksapce.com> - 3.1.1-1.ius
- Building latest 3.1.1

* Thu Feb 03 2011 Jeffrey Ness <jeffrey.ness@racksapce.com> - 2.0.11-2.ius
- Adding python-devel to Build Requires

* Mon Aug 24 2009 BJ Dierkes <wdierkes@rackspace.com> - 2.0.11-1.ius
- Rebuilding for IUS

* Fri Dec 12 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.11-1
- 2.0.11 (2008-12-12)
- Bugs fixed
- 
-    * Crash when using an XPath evaluator in multiple threads.

* Tue Nov 18 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.10-1
- 2.0.10 (2008-11-17)
- Bugs fixed
- 
-    * Ref-count leaks when lxml enters a try-except statement while an
-      outside exception lives in sys.exc_*(). This was due to a problem
-      in Cython, not lxml itself.

* Fri Sep  5 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.9-1
- 2.0.9 (2008-09-05)
- Bugs fixed
- 
-    * Memory problem when passing documents between threads.
-    * Target parser did not honour the recover option and raised an exception
-      instead of calling .close() on the target.

* Fri Jul 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.8-1
- Update to 2.0.8

* Fri Jun 20 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.7-1
- Update to 2.0.7
- Update download URL

* Sat May 31 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.6-1
- Update to 2.0.6

* Thu May  8 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.5-1
- Update to 2.0.5

* Wed Mar 26 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.3-1
- Update to 2.0.3

* Sat Feb 23 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.2-1
- Update to 2.0.2

* Tue Feb 19 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.1-1
- Update to 2.0.1

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.6-2
- Autorebuild for GCC 4.3

* Mon Nov  4 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.3.6-1
- Update to 1.3.6.

* Mon Oct 22 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.3.5-1
- Update to 1.3.5.

* Thu Aug 30 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.3.4-1
- Update to 1.3.4.

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.3.3-3
- Rebuild for selinux ppc32 issue.

* Tue Aug 28 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.3.3-2
- BR python-setuptools-devel

* Mon Jul 30 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.3.3-1
- Update to 1.3.3

* Fri Jan 19 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.2-1
- Update to 1.1.2

* Thu Dec 14 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.0.3-3
- Rebuild for new Python

* Sat Sep 16 2006 Shahms E. King <shahms@shahms.com> 1.0.3-2
- Rebuild for FC6

* Thu Aug 17 2006 Shahms E. King <shahms@shahms.com> 1.0.3-1
- Update to new upstream version

* Fri Aug 11 2006 Shahms E. King <shahms@shahms.com> 1.0.2-2
- Include, don't ghost .pyo files per new guidelines

* Fri Jul 07 2006 Shahms E. King <shahms@shahms.com> 1.0.2-1
- Update to new upstream release

* Mon Jun 26 2006 Shahms E. King <shahms@shahms.com> 1.0.1-1
- Update to new upstream release

* Fri Jun 02 2006 Shahms E. King <shahms@shahms.com> 1.0-1
- Update to new upstream 1.0 release

* Wed Apr 26 2006 Shahms E. King <shahms@shahms.com> 0.9.1-3
- Add python-setuptools to BuildRequires
- Use dist tag

* Wed Apr 26 2006 Shahms E. King <shahms@shahms.com> 0.9.1-2
- Fix summary and description

* Tue Apr 18 2006 Shahms E. King <shahms@shahms.com> 0.9.1-1
- update the new upstream version
- remove Pyrex build req

* Tue Dec 13 2005 Shahms E. King <shahms@shahms.com> 0.8-1
- Initial package
