%define		_class		HTML
%define		_subclass	Common2
%define		upstream_name	%{_class}_%{_subclass}
%define     pre         %{nil}

Name:		php-pear-%{upstream_name}
Version:	2.0.0
Release:	3
Summary:	Abstract base class for HTML classes (PHP5 port of HTML_Common package)
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_Common2/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}%{pre}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
The HTML_Common2 package provides methods for HTML code display and
attributes handling.
- Methods to set, remove, update HTML attributes,
- Handles comments in HTML code.
- Handles global document options (encoding, linebreak and indentation
  characters),
- Handles indentation for nicer HTML code.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}%{pre}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}%{pre}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-2mdv2012.0
+ Revision: 741991
- fix major breakage by careless packager

* Sun May 29 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-1
+ Revision: 681612
- 2.0.0

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-0.beta1.7
+ Revision: 679342
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-0.beta1.6mdv2011.0
+ Revision: 613669
- the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-0.beta1.5mdv2010.1
+ Revision: 477861
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 2.0.0-0.beta1.4mdv2010.0
+ Revision: 441112
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-0.beta1.3mdv2009.1
+ Revision: 322110
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-0.beta1.2mdv2009.0
+ Revision: 236857
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 09 2007 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-0.beta1.1mdv2008.1
+ Revision: 107005
- 2.0.0beta1

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-1mdv2008.0
+ Revision: 15674
- 0.3.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-7mdv2007.0
+ Revision: 81609
- Import php-pear-HTML_Common2

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-1mdk
- initial Mandriva package (PLD import)

