#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-IDN-Encode
Version  : 2.500
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/C/CF/CFAERBER/Net-IDN-Encode-2.500.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CF/CFAERBER/Net-IDN-Encode-2.500.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-idn-encode-perl/libnet-idn-encode-perl_2.400-1.debian.tar.xz
Summary  : 'Internationalizing Domain Names in Applications (UTS #46)'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Net-IDN-Encode-license = %{version}-%{release}
Requires: perl-Net-IDN-Encode-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::NoWarnings)

%description
OVERVIEW
Net::IDN::Encode   -- Internationalized Domain Names in
Applications (IDNA)

%package dev
Summary: dev components for the perl-Net-IDN-Encode package.
Group: Development
Provides: perl-Net-IDN-Encode-devel = %{version}-%{release}
Requires: perl-Net-IDN-Encode = %{version}-%{release}

%description dev
dev components for the perl-Net-IDN-Encode package.


%package license
Summary: license components for the perl-Net-IDN-Encode package.
Group: Default

%description license
license components for the perl-Net-IDN-Encode package.


%package perl
Summary: perl components for the perl-Net-IDN-Encode package.
Group: Default
Requires: perl-Net-IDN-Encode = %{version}-%{release}

%description perl
perl components for the perl-Net-IDN-Encode package.


%prep
%setup -q -n Net-IDN-Encode-2.500
cd %{_builddir}
tar xf %{_sourcedir}/libnet-idn-encode-perl_2.400-1.debian.tar.xz
cd %{_builddir}/Net-IDN-Encode-2.500
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Net-IDN-Encode-2.500/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-IDN-Encode
cp %{_builddir}/Net-IDN-Encode-2.500/LICENSE %{buildroot}/usr/share/package-licenses/perl-Net-IDN-Encode/2f9c36bb77cf37f73a6e820491494f303a761789
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Net-IDN-Encode/890c676b50b181b4066ea4afc96ec3cfdb9d59d3
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::IDN::Encode.3
/usr/share/man/man3/Net::IDN::Overview.3
/usr/share/man/man3/Net::IDN::Punycode.3
/usr/share/man/man3/Net::IDN::Punycode::PP.3
/usr/share/man/man3/Net::IDN::Standards.3
/usr/share/man/man3/Net::IDN::UTS46.3
/usr/share/man/man3/Net::IDN::UTS46::_Mapping.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-IDN-Encode/2f9c36bb77cf37f73a6e820491494f303a761789
/usr/share/package-licenses/perl-Net-IDN-Encode/890c676b50b181b4066ea4afc96ec3cfdb9d59d3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Net/IDN/Encode.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/IDN/Overview.pod
/usr/lib/perl5/vendor_perl/5.30.3/Net/IDN/Punycode.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/IDN/Punycode.xs
/usr/lib/perl5/vendor_perl/5.30.3/Net/IDN/Punycode/PP.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/IDN/Standards.pod
/usr/lib/perl5/vendor_perl/5.30.3/Net/IDN/UTS46.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/IDN/UTS46/_Mapping.pm
