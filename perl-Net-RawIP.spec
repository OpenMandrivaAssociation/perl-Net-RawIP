%define pkgname Net-RawIP

Summary:	Net::RawIP - a perl module can to manipulate raw IP packets
Name:		perl-%{pkgname}
Version:	0.2
Release:    %mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{pkgname}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{pkgname}-%{version}.tar.bz2
Patch0:		Net-RawIP-0.2-nolvaluecast.patch
BuildRequires:	perl-devel
BuildRequires:	libpcap-devel
Buildroot:	%{_tmppath}/%{name}-buildroot

%description
This is Net::RawIP, a perl module can to manipulate raw IP packets,
with an optional feature for manipulating Ethernet headers.

%prep

%setup -q -n %{pkgname}-%{version}
%patch0 -p0 -b .nolvaluecast

# fix attribs
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

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
%dir %{perl_vendorarch}/auto/Net/RawIP
%{perl_vendorarch}/auto/Net/RawIP/RawIP.so
%{perl_vendorarch}/auto/Net/RawIP/autosplit.ix
%{perl_vendorarch}/Net/RawIP.pm
%dir %{perl_vendorarch}/Net/RawIP
%{perl_vendorarch}/Net/RawIP/libpcap.pod
%{_mandir}/*/*

