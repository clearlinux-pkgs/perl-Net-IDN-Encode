#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-IDN-Encode
Version  : 2.500
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/C/CF/CFAERBER/Net-IDN-Encode-2.500.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CF/CFAERBER/Net-IDN-Encode-2.500.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-idn-encode-perl/libnet-idn-encode-perl_2.400-1.debian.tar.xz
Summary  : 'Internationalizing Domain Names in Applications (UTSÂ #46)'
Group    : Development/Tools
License  : Artistic-1.0-Perl
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

%description dev
dev components for the perl-Net-IDN-Encode package.


%prep
%setup -q -n Net-IDN-Encode-2.500
cd ..
%setup -q -T -D -n Net-IDN-Encode-2.500 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Net-IDN-Encode-2.500/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Net/IDN/Encode.pm
/usr/lib/perl5/site_perl/5.26.1/Net/IDN/Overview.pod
/usr/lib/perl5/site_perl/5.26.1/Net/IDN/Punycode.pm
/usr/lib/perl5/site_perl/5.26.1/Net/IDN/Punycode.xs
/usr/lib/perl5/site_perl/5.26.1/Net/IDN/Punycode/PP.pm
/usr/lib/perl5/site_perl/5.26.1/Net/IDN/Standards.pod
/usr/lib/perl5/site_perl/5.26.1/Net/IDN/UTS46.pm
/usr/lib/perl5/site_perl/5.26.1/Net/IDN/UTS46/_Mapping.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::IDN::Encode.3
/usr/share/man/man3/Net::IDN::Overview.3
/usr/share/man/man3/Net::IDN::Punycode.3
/usr/share/man/man3/Net::IDN::Punycode::PP.3
/usr/share/man/man3/Net::IDN::Standards.3
/usr/share/man/man3/Net::IDN::UTS46.3
/usr/share/man/man3/Net::IDN::UTS46::_Mapping.3
