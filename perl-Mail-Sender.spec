#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	Sender
Summary:	Mail::Sender - sending mails with attachments through an SMTP server
Summary(pl):	Mail::Sender - wysy³anie poczty z za³±cznikami za po¶rednictwem serwera SMTP
Name:		perl-Mail-Sender
Version:	0.8.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4dac1115bacca2ed0b8403c3874975da
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
Mail::Sender udostêpnia zorientowany obiektowo interfejs do wysy³ania
poczty. Nie potrzebuje ¿adnego zewnêtrznego programu. £±czy siê
bezpo¶rednio z Perla z serwerem, korzystaj±c z modu³u Socket.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} </dev/null

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
