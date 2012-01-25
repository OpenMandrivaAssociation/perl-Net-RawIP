%define upstream_name    Net-RawIP
%define upstream_version 0.25

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

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
