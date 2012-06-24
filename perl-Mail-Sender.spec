%include	/usr/lib/rpm/macros.perl
Summary:	Mail-Sender perl module
Summary(pl):	Modu� perla Mail-Sender
Name:		perl-Mail-Sender
Version:	0.7.04
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mail/Mail-Sender-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-MIME-Base64
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail-Sender is a module for sending mails with attachments through an
SMTP server.

%description -l pl
Mail-Sender jest modu�em s�u��cym do wysy�ania poczty z za��cznikami
przez serwer SMTP.

%prep
%setup -q -n Mail-Sender-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Mail/Sender
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Mail/Sender.pm
%{perl_sitearch}/auto/Mail/Sender

%{_mandir}/man3/*
