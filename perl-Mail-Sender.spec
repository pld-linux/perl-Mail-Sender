%include	/usr/lib/rpm/macros.perl
Summary:	Mail-Sender perl module
Summary(pl):	Modu³ perla Mail-Sender
Name:		perl-Mail-Sender
Version:	0.7.08
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mail/Mail-Sender-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-MIME-Base64
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail-Sender is a module for sending mails with attachments through an
SMTP server.

%description -l pl
Mail-Sender jest modu³em s³u¿±cym do wysy³ania poczty z za³±cznikami
przez serwer SMTP.

%prep
%setup -q -n Mail-Sender-%{version}

%build
perl Makefile.PL
yes "" | %{__make}

%install
rm -rf $RPM_BUILD_ROOT

yes "" | %{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Mail/Sender.pm
%{_mandir}/man3/*
