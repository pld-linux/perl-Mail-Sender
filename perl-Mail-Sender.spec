%include	/usr/lib/rpm/macros.perl
Summary:	Mail-Sender perl module
Summary(pl):	Modu� perla Mail-Sender
Name:		perl-Mail-Sender
Version:	0.7.10
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mail/Mail-Sender-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-MIME-Base64
BuildArch:	noarch
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
