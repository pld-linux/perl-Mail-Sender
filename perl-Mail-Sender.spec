%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	Sender
Summary:	Mail::Sender perl module
Summary(pl):	Modu³ perla Mail::Sender
Name:		perl-Mail-Sender
Version:	0.7.13.1
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-MIME-Base64
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail::Sender is a module for sending mails with attachments through an
SMTP server.

%description -l pl
Mail::Sender jest modu³em s³u¿±cym do wysy³ania poczty z za³±cznikami
przez serwer SMTP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
yes "" | %{__make}

%install
rm -rf $RPM_BUILD_ROOT

yes "" | %{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Mail/Sender.pm
%{_mandir}/man3/*
