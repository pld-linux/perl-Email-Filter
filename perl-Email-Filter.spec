#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Email
%define		pnam	Filter
Summary:	Email::Filter - library for creating easy email filters
Summary(pl):	Email::Filter - biblioteka do tworzenia prostych filtrów dla poczty
Name:		perl-Email-Filter
Version:	1.01
Release:	1
License:	BSD, Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9186286616c6fb6a7d8a67ea5b2ae555
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Trigger
BuildRequires:	perl-Email-LocalDelivery >= 0.04
BuildRequires:	perl-Email-Simple >= 1.1
BuildRequires:	perl-IPC-Run
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is another module produced by the "Perl Email Project", a reaction
against the complexity and increasing bugginess of the "Mail::*"
modules. It replaces Mail::Audit, and allows you to write programs
describing how your mail should be filtered.

%description -l pl
To jest kolejny modu³ wyprodukowany przez "Perl Email Project", bêd±cy
reakcj± na z³o¿ono¶æ i rosn±cy wspó³czynnik zapluskwienia modu³ów
Mail::*. Zastêpuje Mail::Audit i pozwala na pisanie programów
opisuj±cych jak poczta powinna byæ filtrowana.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
