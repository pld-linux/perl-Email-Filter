#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Email
%define		pnam	Filter
Summary:	Email::Filter - library for creating easy email filters
Summary(pl.UTF-8):	Email::Filter - biblioteka do tworzenia prostych filtrów dla poczty
Name:		perl-Email-Filter
Version:	1.034
Release:	1
License:	BSD, Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2b49d6892f81e8d93fd8e1df6f74e580
URL:		http://search.cpan.org/dist/Email-Filter/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Trigger >= 0.08
BuildRequires:	perl-Email-LocalDelivery >= 0.07
BuildRequires:	perl-Email-Simple >= 1:1.91
BuildRequires:	perl-IPC-Run >= 0.77
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is another module produced by the "Perl Email Project", a
reaction against the complexity and increasing bugginess of the
"Mail::*" modules. It replaces Mail::Audit, and allows you to write
programs describing how your mail should be filtered.

%description -l pl.UTF-8
To jest kolejny moduł wyprodukowany przez "Perl Email Project", będący
reakcją na złożoność i rosnący współczynnik zapluskwienia modułów
Mail::*. Zastępuje Mail::Audit i pozwala na pisanie programów
opisujących jak poczta powinna być filtrowana.

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
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
