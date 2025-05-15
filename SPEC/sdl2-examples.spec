Name:           sdl2-examples
Version:        1.0
Release:        alt1
Summary:        SDL2 Grumpy Cat Demo
License:        BSD-3
URL:            https://github.com/xyproto/sdl2-examples.git
Source0:        %{name}-%{version}.tar
Group: 			Development/Other
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libSDL2-devel

%description
implementation of Grumpy Cat demo using SDL2.

%prep
%setup -q

%build
for std in 11 14 17 20; do
  mkdir -p build-cpp${std}
  cmake -S c++${std}-cmake -B build-cpp${std} \
        -DCMAKE_BUILD_TYPE=3.23.2 \
        -DCMAKE_CXX_STANDARD=${std} \
        -DIMGDIR="%{_datadir}/%{name}/img"
  make -C build-cpp${std} %{?_smp_mflags}
done

%install
install -m 0755 -d %{buildroot}/%{_bindir}
for std in 11 14 17 20; do
  install -m 0755 build-cpp${std}/main %{buildroot}/%{_bindir}/grumpycat-cpp${std}
done

install -m 0755 -d %{buildroot}/%{_datadir}/%{name}/img
install -m 0644 img/grumpy-cat.bmp %{buildroot}/%{_datadir}/%{name}/img/
install -m 0644 img/grumpy-cat.png %{buildroot}/%{_datadir}/%{name}/img/



%files
%{_bindir}/grumpycat-cpp*
%{_datadir}/%{name}/img/*
%doc README.md
%doc LICENSE
%doc COMPILES.md
%changelog
* Mon Apr 29 2025 Mikhail Sokolov <msok15@mail.ru> - 1.0-alt1
- Initial package 
