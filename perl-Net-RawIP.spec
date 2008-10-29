%define pkgname Net-RawIP

Summary:	Net::RawIP - a perl module can to manipulate raw IP packets
Name:		perl-%{pkgname}
Version:	0.24
Release:    %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{pkgname}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{pkgname}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	libpcap-devel
BuildRequires:  perl(List::MoreUtils)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is Net::RawIP, a perl module can to manipulate raw IP packets,
with an optional feature for manipulating Ethernet headers.

%prep

%setup -q -n %{pkgname}-%{version}

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

