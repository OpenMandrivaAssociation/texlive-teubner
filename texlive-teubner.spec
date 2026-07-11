%global tl_name teubner
%global tl_revision 68074

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.8.3
Release:	%{tl_revision}.1
Summary:	Philological typesetting of classical Greek
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/teubner
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/teubner.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/teubner.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/teubner.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An extension to babel greek option for typesetting classical Greek with
a philological approach. The package works with the author's greek fonts
using the 'Lispiakos' font shape derived from that of the fonts used in
printers' shops in Lispia. The package name honours the publisher B.G.
Teubner Verlaggesellschaft whose Greek text publications are of high
quality.

