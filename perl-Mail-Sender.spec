#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	Sender
Summary:	Mail::Sender Perl module
Summary(cs):	Modul Mail::Sender pro Perl
Summary(da):	Perlmodul Mail::Sender
Summary(de):	Mail::Sender Perl Modul
Summary(es):	Módulo de Perl Mail::Sender
Summary(fr):	Module Perl Mail::Sender
Summary(it):	Modulo di Perl Mail::Sender
Summary(ja):	Mail::Sender Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Mail::Sender ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Mail::Sender
Summary(pl):	Modu³ Perla Mail::Sender
Summary(pt):	Módulo de Perl Mail::Sender
Summary(pt_BR):	Módulo Perl Mail::Sender
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Mail::Sender
Summary(sv):	Mail::Sender Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Mail::Sender
Summary(zh_CN):	Mail::Sender Perl Ä£¿é
Name:		perl-Mail-Sender
Version:	0.8.05
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-MIME-Base64
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Mail::Sender.config)'

%description
Mail::Sender is a module for sending mails with attachments through an
SMTP server.

%description -l pl
Mail::Sender jest modu³em s³u¿±cym do wysy³ania poczty z za³±cznikami
przez serwer SMTP.

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
