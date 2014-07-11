# revision 32527
# category Package
# catalog-ctan /macros/latex/contrib/teubner
# catalog-date 2013-12-31 15:44:59 +0100
# catalog-license lppl
# catalog-version 4.2
Name:		texlive-teubner
Version:	4.2
Release:	3
Summary:	Philological typesetting of classical Greek
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/teubner
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/teubner.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/teubner.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/teubner.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
An extension to babel greek option for typesetting classical
Greek with a philological approach. The package works with the
author's greek fonts using the 'Lispiakos' font shape derived
from that of the fonts used in printers' shops in Lispia. The
package name honours the publisher B.G. Teubner
Verlaggesellschaft whose Greek text publications are of high
quality.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/teubner/teubner.sty
%{_texmfdistdir}/tex/latex/teubner/teubnertx.sty
%doc %{_texmfdistdir}/doc/latex/teubner/README
%doc %{_texmfdistdir}/doc/latex/teubner/teubner-doc.pdf
%doc %{_texmfdistdir}/doc/latex/teubner/teubner-doc.tex
%doc %{_texmfdistdir}/doc/latex/teubner/teubner.pdf
%doc %{_texmfdistdir}/doc/latex/teubner/teubner.txt
#- source
%doc %{_texmfdistdir}/source/latex/teubner/teubner.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
