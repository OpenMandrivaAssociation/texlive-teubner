# revision 23854
# category Package
# catalog-ctan /macros/latex/contrib/teubner
# catalog-date 2011-09-07 11:50:17 +0200
# catalog-license lppl
# catalog-version 3.3
Name:		texlive-teubner
Version:	3.3
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
An extension to babel greek option for typesetting classical
Greek with a philological approach. The package works with the
author's greek fonts using the 'Lispiakos' font shape derived
from that of the fonts used in printers' shops in Lispia. The
package name honours the publisher B.G. Teubner
Verlaggesellschaft whose Greek text publications are of high
quality.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/teubner/LGRaccents-glyphs.def
%{_texmfdistdir}/tex/latex/teubner/teubner.sty
%{_texmfdistdir}/tex/latex/teubner/teubnertx.sty
%doc %{_texmfdistdir}/doc/latex/teubner/README
%doc %{_texmfdistdir}/doc/latex/teubner/teubner-doc.pdf
%doc %{_texmfdistdir}/doc/latex/teubner/teubner-doc.tex
%doc %{_texmfdistdir}/doc/latex/teubner/teubner.pdf
%doc %{_texmfdistdir}/doc/latex/teubner/teubner.txt
#- source
%doc %{_texmfdistdir}/source/latex/teubner/teubner.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
