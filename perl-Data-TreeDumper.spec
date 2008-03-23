#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	TreeDumper
Summary:	Data::TreeDumper - Perl module for dumping data structures
Summary(pl.UTF-8):	Data::TreeDumper - moduł Perla do zrzucania struktur danych
Name:		perl-Data-TreeDumper
Version:	0.33
Release:	1
# same as perl 
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e6ca587679f0961393b1c45a6f92eb0b
URL:		http://search.cpan.org/dist/Data-TreeDumper/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Devel-Size >= 0.58
BuildRequires:	perl-Sort-Naturally
BuildRequires:	perl-Term-Size >= 0.2
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Dumper and other modules do a great job of dumping data
structures. Their output, however, often takes more brain power to
understand than the data itself. When dumping large amounts of data,
the output can be overwhelming and it can be difficult to see the
relationship between each piece of the dumped data.

Data::TreeDumper also dumps data in a tree-like fashion but hopefully
in a format more easily understood.

%description -l pl.UTF-8
Data::Dumper i inne moduły wykonują wspaniałe zadanie zrzucania
struktur danych. Ich wyjście jednak zwykle wymaga trochę wysiłku
umysłowego do zrozumienia danych. Przy zrzucaniu dużej ilości
danych wyjście może być zbyt skomplikowane, żeby zobaczyć powiązania
między danymi.

Data::TreeDumper także zrzuca dane w postaci podobnej do drzewa, ale w
formacie, który powinien być łatwiejszy do zrozumienia.

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT%{perl_vendorlib}/Data/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Data/*.pm
%dir %{perl_vendorlib}/auto/Data/TreeDumper
%{perl_vendorlib}/auto/Data/TreeDumper/autosplit.ix
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
