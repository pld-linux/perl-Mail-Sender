#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	Sender
Summary:	Mail::Sender - module for sending mails with attachments through an SMTP server
Summary(pl):	Mail::Sender - modu³ s³u¿±cy do wysy³ania poczty z za³±cznikami za po¶rednictwem serwera SMTP
Name:		perl-Mail-Sender
Version:	0.8.06
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-MIME-Base64
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Mail::Sender.config)' 'perl(Authen::NTLM)' 'perl(Digest::HMAC_MD5)'

%description
Mail::Sender provides an object oriented interface to sending mails.
It doesn't need any outer program. It connects to a mail server
directly from Perl, using Socket.

%description -l pl
Mail::Sender udostêpnia zorientowany obiektowo interfejs do wysy³ania
poczty. Nie potrzebuje ¿adnego zewnêtrznego programu. £±czy siê
bezpo¶rednio z Perla z serwerem, korzystaj±c z modu³u Socket.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} </dev/null

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Mail/Sender.pm
%{_mandir}/man3/*
