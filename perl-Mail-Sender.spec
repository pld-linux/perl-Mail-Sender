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
Summary(es):	M�dulo de Perl Mail::Sender
Summary(fr):	Module Perl Mail::Sender
Summary(it):	Modulo di Perl Mail::Sender
Summary(ja):	Mail::Sender Perl �⥸�塼��
Summary(ko):	Mail::Sender �� ����
Summary(no):	Perlmodul Mail::Sender
Summary(pl):	Modu� Perla Mail::Sender
Summary(pt):	M�dulo de Perl Mail::Sender
Summary(pt_BR):	M�dulo Perl Mail::Sender
Summary(ru):	������ ��� Perl Mail::Sender
Summary(sv):	Mail::Sender Perlmodul
Summary(uk):	������ ��� Perl Mail::Sender
Summary(zh_CN):	Mail::Sender Perl ģ��
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
Mail::Sender jest modu�em s�u��cym do wysy�ania poczty z za��cznikami
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
