#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Mail
%define		pnam	Sender
Summary:	Mail::Sender - sending mails with attachments through an SMTP server
Summary(pl.UTF-8):	Mail::Sender - wysyłanie poczty z załącznikami za pośrednictwem serwera SMTP
Name:		perl-Mail-Sender
Version:	0.903
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mail/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	56f391635683d0edf4f992ab9368ed61
URL:		http://search.cpan.org/dist/Mail-Sender/
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Mail::Sender.config)' 'perl(Authen::NTLM)' 'perl(Digest::HMAC_MD5)'

%description
Mail::Sender provides an object oriented interface to sending mails.
It doesn't need any outer program. It connects to a mail server
directly from Perl, using Socket.

%description -l pl.UTF-8
Mail::Sender udostępnia zorientowany obiektowo interfejs do wysyłania
poczty. Nie potrzebuje żadnego zewnętrznego programu. Łączy się
bezpośrednio z Perla z serwerem, korzystając z modułu Socket.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} </dev/null

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Mail/Sender.pm
%{perl_vendorlib}/Mail/Sender
%{_mandir}/man3/*
