%define		oname	wxWidgets
%define		api	3.0
%define		major	0

Summary:	GTK+ port of the wxWidgets library
Name:		wxgtk%{api}
Version:	3.0.2
Release:	3
License:	wxWidgets Library Licence
Group:		System/Libraries
Url:		http://www.wxwidgets.org/
Source0:	http://prdownloads.sourceforge.net/wxwindows/%{oname}-%{version}.tar.bz2
Patch0:		wxWidgets-3.0.0-locales.patch
Patch1:		gst1.0.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
# GTK3 leads to conflicting declarations etc for wx-based applications
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(webkit-1.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(zlib)

%description
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

%files -f wxstd-%{api}.lang
%doc *.txt

#----------------------------------------------------------------------------

%define libwx_baseu %mklibname wx_baseu %{api} %{major}

%package -n	%{libwx_baseu}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_baseu}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_baseu}
%{_libdir}/libwx_baseu-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_baseu_net %mklibname wx_baseu_net %{api} %{major}

%package -n	%{libwx_baseu_net}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_baseu_net}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_baseu_net}
%{_libdir}/libwx_baseu_net-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_baseu_xml %mklibname wx_baseu_xml %{api} %{major}

%package -n	%{libwx_baseu_xml}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_baseu_xml}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_baseu_xml}
%{_libdir}/libwx_baseu_xml-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_adv %mklibname wx_gtk2u_adv %{api} %{major}

%package -n	%{libwx_gtk2u_adv}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_adv}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_adv}
%{_libdir}/libwx_gtk2u_adv-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_aui %mklibname wx_gtk2u_aui %{api} %{major}

%package -n	%{libwx_gtk2u_aui}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_aui}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_aui}
%{_libdir}/libwx_gtk2u_aui-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_core %mklibname wx_gtk2u_core %{api} %{major}

%package -n	%{libwx_gtk2u_core}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_core}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_core}
%{_libdir}/libwx_gtk2u_core-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_gl %mklibname wx_gtk2u_gl %{api} %{major}

%package -n	%{libwx_gtk2u_gl}
Summary:	OpenGL shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_gl}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_gl}
%{_libdir}/libwx_gtk2u_gl-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_html %mklibname wx_gtk2u_html %{api} %{major}

%package -n	%{libwx_gtk2u_html}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_html}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_html}
%{_libdir}/libwx_gtk2u_html-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_media %mklibname wx_gtk2u_media %{api} %{major}

%package -n	%{libwx_gtk2u_media}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_media}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_media}
%{_libdir}/libwx_gtk2u_media-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_propgrid %mklibname wx_gtk2u_propgrid %{api} %{major}

%package -n	%{libwx_gtk2u_propgrid}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_propgrid}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_propgrid}
%{_libdir}/libwx_gtk2u_propgrid-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_qa %mklibname wx_gtk2u_qa %{api} %{major}

%package -n	%{libwx_gtk2u_qa}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_qa}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_qa}
%{_libdir}/libwx_gtk2u_qa-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_ribbon %mklibname wx_gtk2u_ribbon %{api} %{major}

%package -n	%{libwx_gtk2u_ribbon}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_ribbon}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_ribbon}
%{_libdir}/libwx_gtk2u_ribbon-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_richtext %mklibname wx_gtk2u_richtext %{api} %{major}

%package -n	%{libwx_gtk2u_richtext}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_richtext}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_richtext}
%{_libdir}/libwx_gtk2u_richtext-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_stc %mklibname wx_gtk2u_stc %{api} %{major}

%package -n	%{libwx_gtk2u_stc}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_stc}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_stc}
%{_libdir}/libwx_gtk2u_stc-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_webview %mklibname wx_gtk2u_webview %{api} %{major}

%package -n	%{libwx_gtk2u_webview}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_webview}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_webview}
%{_libdir}/libwx_gtk2u_webview-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_xrc %mklibname wx_gtk2u_xrc %{api} %{major}

%package -n	%{libwx_gtk2u_xrc}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_xrc}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_xrc}
%{_libdir}/libwx_gtk2u_xrc-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libnameudev %mklibname -d wxgtku %{api}

%package -n	%{libnameudev}
Summary:	Header files and development documentation for wxGTK - unicode
Group:		Development/C++
Requires:	%{libwx_baseu} = %{EVRD}
Requires:	%{libwx_baseu_net} = %{EVRD}
Requires:	%{libwx_baseu_xml} = %{EVRD}
Requires:	%{libwx_gtk2u_adv} = %{EVRD}
Requires:	%{libwx_gtk2u_aui} = %{EVRD}
Requires:	%{libwx_gtk2u_core} = %{EVRD}
Requires:	%{libwx_gtk2u_gl} = %{EVRD}
Requires:	%{libwx_gtk2u_html} = %{EVRD}
Requires:	%{libwx_gtk2u_media} = %{EVRD}
Requires:	%{libwx_gtk2u_propgrid} = %{EVRD}
Requires:	%{libwx_gtk2u_qa} = %{EVRD}
Requires:	%{libwx_gtk2u_ribbon} = %{EVRD}
Requires:	%{libwx_gtk2u_richtext} = %{EVRD}
Requires:	%{libwx_gtk2u_stc} = %{EVRD}
Requires:	%{libwx_gtk2u_webview} = %{EVRD}
Requires:	%{libwx_gtk2u_xrc} = %{EVRD}
Provides:	wxgtku%{api}-devel = %{EVRD}
# At this time 2.8 and 3.0 cannot co-exist because of file conflicts
Conflicts:	%{_lib}wxgtku2.8-devel

%description -n %{libnameudev}
Header files for the unicode enabled version of wxGTK, the GTK+ port of
the wxWidgets library.

%files -n %{libnameudev}
%doc samples/
%doc docs/
%doc demos/
%{_bindir}/wx-config
%{_bindir}/wxrc
%{_bindir}/wxrc-%{api}
%{_includedir}/wx-%{api}/
%{_datadir}/aclocal/*
%{_datadir}/bakefile/
%{_libdir}/wx/config/gtk2-unicode-%{api}
%{_libdir}/wx/include/gtk2-unicode-%{api}/wx/setup.h
%{_libdir}/libwx_baseu-%{api}.so
%{_libdir}/libwx_baseu_net-%{api}.so
%{_libdir}/libwx_baseu_xml-%{api}.so
%{_libdir}/libwx_gtk2u_adv-%{api}.so
%{_libdir}/libwx_gtk2u_aui-%{api}.so
%{_libdir}/libwx_gtk2u_core-%{api}.so
%{_libdir}/libwx_gtk2u_gl-%{api}.so
%{_libdir}/libwx_gtk2u_html-%{api}.so
%{_libdir}/libwx_gtk2u_media-%{api}.so
%{_libdir}/libwx_gtk2u_propgrid-%{api}.so
%{_libdir}/libwx_gtk2u_qa-%{api}.so
%{_libdir}/libwx_gtk2u_ribbon-%{api}.so
%{_libdir}/libwx_gtk2u_richtext-%{api}.so
%{_libdir}/libwx_gtk2u_stc-%{api}.so
%{_libdir}/libwx_gtk2u_webview-%{api}.so
%{_libdir}/libwx_gtk2u_xrc-%{api}.so

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1
%patch1 -p1
sh autogen.sh
#autoreconf -fiv -I `pwd`/build/aclocal
# fix plugin dir for 64-bit
sed -i -e 's|/lib|/%{_lib}|' src/unix/stdpaths.cpp

%build
#gw 2.8.11 doesn't build otherwise:
%define _disable_ld_no_undefined 1
%define Werror_cflags %nil
# --disable-optimise prevents our $RPM_OPT_FLAGS being overridden
# (see OPTIMISE in configure).
# this code dereferences type-punned pointers like there's no tomorrow.
CFLAGS="%{optflags} -fno-strict-aliasing"
CXXFLAGS="%{optflags} -fno-strict-aliasing"

%configure --enable-unicode \
	--enable-compat28 \
	--without-odbc \
	--with-opengl \
	--enable-gtk2 --with-gtk  \
	--without-debug_flag \
	--without-debug_info \
	--with-sdl \
	--with-libpng=sys \
	--with-libjpeg=sys \
	--with-libtiff=sys \
	--with-zlib=sys \
	--disable-optimise \
	--enable-calendar \
	--enable-wave \
	--enable-fraction \
	--enable-wxprintfv \
	--enable-xresources \
	--enable-controls \
	--enable-tabdialog \
	--enable-msgdlg \
	--enable-dirdlg \
	--enable-numberdlg \
	--enable-splash \
	--enable-textdlg \
	--enable-graphics_ctx \
	--enable-grid \
	--disable-catch_segvs \
	--enable-mediactrl \
	--enable-dataviewctrl

%make

# make -C locale

%install
%makeinstall_std
%find_lang wxstd-%{api}
%find_lang wxmsw-%{api}
cat wxmsw-%{api}.lang >> wxstd-%{api}.lang

