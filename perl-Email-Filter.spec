#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Filter
Summary:	Email::Filter - Library for creating easy email filters
#Summary(pl):	
Name:		perl-Email-Filter
Version:	1.0
Release:	1
License:	BSD, Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	857a522c2c43991f59c65de9c8c05d40
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
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

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

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
