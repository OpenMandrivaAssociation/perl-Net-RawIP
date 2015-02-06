%define upstream_name    Net-RawIP
%define upstream_version 0.25

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:	Net::RawIP - a perl module can to manipulate raw IP packets
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	libpcap-devel
BuildRequires:  perl(List::MoreUtils)
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is Net::RawIP, a perl module can to manipulate raw IP packets,
with an optional feature for manipulating Ethernet headers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

# fix attribs
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

perl -pi -e 's!/usr/lib!%{_libdir}!g' Makefile.PL

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README README.Devel examples
%{perl_vendorarch}/auto/Net
%{perl_vendorarch}/Net
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.250.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.250.0-1mdv2010.0
+ Revision: 407839
- rebuild using %%perl_convert_version

* Fri Oct 31 2008 Olivier Thauvin <nanardon@mandriva.org> 0.25-1mdv2009.1
+ Revision: 299091
- 0.25

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.24-2mdv2009.1
+ Revision: 298349
- rebuilt against libpcap-1.0.0

* Wed Oct 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-1mdv2009.1
+ Revision: 296398
- update to new version 0.24

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.23-4mdv2009.0
+ Revision: 258093
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.23-3mdv2009.0
+ Revision: 246166
- rebuild

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdv2008.1
+ Revision: 156652
- new version

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.21-2mdv2008.1
+ Revision: 152226
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 0.21-1mdv2008.0
+ Revision: 20300
- 0.21


* Sat Sep 02 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-02 18:38:22 (59622)
- test in check section

* Sat Sep 02 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-02 18:34:58 (59621)
Import perl-Net-RawIP

* Fri Apr 28 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.2-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Wed Oct 05 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.2-1mdk
- initial Mandriva package

