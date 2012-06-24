#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	Sender
Summary:	Mail::Sender - sending mails with attachments through an SMTP server
Summary(pl):	Mail::Sender - wysy�anie poczty z za��cznikami za po�rednictwem serwera SMTP
Name:		perl-Mail-Sender
Version:	0.8.08
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6076c4fbaf6a285a406daa4e84b0cf7d
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-MIME-Base64
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Mail::Sender.config)' 'perl(Authen::NTLM)' 'perl(Digest::HMAC_MD5)'

%description
Mail::Sender provides an object oriented interface to sending mails.
It doesn't need any outer program. It connects to a mail server
directly from Perl, using Socket.

%description -l pl
Mail::Sender udost�pnia zorientowany obiektowo interfejs do wysy�ania
poczty. Nie potrzebuje �adnego zewn�trznego programu. ��czy si�
bezpo�rednio z Perla z serwerem, korzystaj�c z modu�u Socket.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%{perl_vendorlib}/Mail/Sender.pm
%{_mandir}/man3/*
