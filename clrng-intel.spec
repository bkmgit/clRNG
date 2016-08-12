Name: clrng-intel
Version: 4a16519git  
Release: 1%{?dist}
Summary: clRNG for Intel processors using Beignet runtime on Fedora 24

License: Apache License, Version 2.0
URL: https://github.com/clMathLibraries/clRNG
Source0: https://github.com/clMathLibraries/clRNG/archive/master.zip 

BuildRequires: cmake
BuildRequires: beignet-devel
BuildRequires: ocl-icd-devel

%description
clRNG is a library that can make use of GPUs to offload random number generation subroutine libraries. The version here is built using the Intel Beignet openCL runtime which will work on 
Intel CPUs with integrated GPUs.

%prep
rm -rf clRNG-master
unzip %{SOURCE0}

%build
cmake clRNG-master/src/  -DCMAKE_BUILD_TYPE=Debug 
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%check
ctest -V %{?_smp_mflags}

%clean
rm -rf %{buildroot} 

%files
/builddir/build/BUILD/package/bin/CTest
/builddir/build/BUILD/package/bin/CTest-1.0.0
/builddir/build/BUILD/package/bin/HostOnly
/builddir/build/BUILD/package/bin/HostOnly-1.0.0
/builddir/build/BUILD/package/bin/Inventory
/builddir/build/BUILD/package/bin/Inventory-1.0.0
/builddir/build/BUILD/package/bin/MultiStream
/builddir/build/BUILD/package/bin/MultiStream-1.0.0
/builddir/build/BUILD/package/bin/RandomArray
/builddir/build/BUILD/package/bin/RandomArray-1.0.0
/builddir/build/BUILD/package/bin/WorkItem
/builddir/build/BUILD/package/bin/WorkItem-1.0.0
/builddir/build/BUILD/package/client/Inventory/InventoryKernels.cl
/builddir/build/BUILD/package/client/WorkItem/workitem_kernel.cl
/builddir/build/BUILD/package/include/clRNG/clRNG.clh
/builddir/build/BUILD/package/include/clRNG/clRNG.h
/builddir/build/BUILD/package/include/clRNG/clRNG.version.h
/builddir/build/BUILD/package/include/clRNG/lfsr113.clh
/builddir/build/BUILD/package/include/clRNG/lfsr113.h
/builddir/build/BUILD/package/include/clRNG/mrg31k3p.clh
/builddir/build/BUILD/package/include/clRNG/mrg31k3p.h
/builddir/build/BUILD/package/include/clRNG/mrg32k3a.clh
/builddir/build/BUILD/package/include/clRNG/mrg32k3a.h
/builddir/build/BUILD/package/include/clRNG/philox432.clh
/builddir/build/BUILD/package/include/clRNG/philox432.h
/builddir/build/BUILD/package/include/clRNG/private/Random123/array.h
/builddir/build/BUILD/package/include/clRNG/private/Random123/features/clangfeatures.h
/builddir/build/BUILD/package/include/clRNG/private/Random123/features/compilerfeatures.h
/builddir/build/BUILD/package/include/clRNG/private/Random123/features/gccfeatures.h
/builddir/build/BUILD/package/include/clRNG/private/Random123/features/msvcfeatures.h
/builddir/build/BUILD/package/include/clRNG/private/Random123/features/open64features.h
/builddir/build/BUILD/package/include/clRNG/private/Random123/features/openclfeatures.h
/builddir/build/BUILD/package/include/clRNG/private/Random123/features/sse.h
/builddir/build/BUILD/package/include/clRNG/private/Random123/philox.h
/builddir/build/BUILD/package/include/clRNG/private/lfsr113.c.h
/builddir/build/BUILD/package/include/clRNG/private/modular.c.h
/builddir/build/BUILD/package/include/clRNG/private/mrg31k3p.c.h
/builddir/build/BUILD/package/include/clRNG/private/mrg32k3a.c.h
/builddir/build/BUILD/package/include/clRNG/private/philox432.c.h
/builddir/build/BUILD/package/lib64/cmake/clRNG/clRNG-Targets-debug.cmake
/builddir/build/BUILD/package/lib64/cmake/clRNG/clRNG-Targets.cmake
/builddir/build/BUILD/package/lib64/cmake/clRNG/clRNGConfig.cmake
/builddir/build/BUILD/package/lib64/cmake/clRNG/clRNGConfigVersion.cmake
/builddir/build/BUILD/package/lib64/libclRNG.so
/builddir/build/BUILD/package/lib64/libclRNG.so.1
/builddir/build/BUILD/package/lib64/libclRNG.so.1.0.0
/builddir/build/BUILD/package/lib64/pkgconfig/clRNG.pc
/builddir/build/BUILD/package/lib64/src/CMakeLists.txt
/builddir/build/BUILD/package/lib64/src/FindOpenCL.cmake
/builddir/build/BUILD/package/lib64/src/client/CMakeLists.txt
/builddir/build/BUILD/package/lib64/src/client/HostOnly/hostonly.c
/builddir/build/BUILD/package/lib64/src/client/Inventory/InventoryKernels.cl
/builddir/build/BUILD/package/lib64/src/client/Inventory/Policies.c
/builddir/build/BUILD/package/lib64/src/client/Inventory/Policies.h
/builddir/build/BUILD/package/lib64/src/client/Inventory/SimulateRuns.c
/builddir/build/BUILD/package/lib64/src/client/Inventory/SimulateRuns.h
/builddir/build/BUILD/package/lib64/src/client/Inventory/Types.h
/builddir/build/BUILD/package/lib64/src/client/Inventory/inventory.c
/builddir/build/BUILD/package/lib64/src/client/MultiStream/multistream.c
/builddir/build/BUILD/package/lib64/src/client/RandomArray/randomarray.c
/builddir/build/BUILD/package/lib64/src/client/WorkItem/workitem.c
/builddir/build/BUILD/package/lib64/src/client/WorkItem/workitem_kernel.cl
/builddir/build/BUILD/package/lib64/src/client/anyrng.h
/builddir/build/BUILD/package/lib64/src/client/common.c
/builddir/build/BUILD/package/lib64/src/client/common.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/clRNG.clh
/builddir/build/BUILD/package/lib64/src/include/clRNG/clRNG.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/clRNG.version.h.in
/builddir/build/BUILD/package/lib64/src/include/clRNG/clRNG_template.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/lfsr113.clh
/builddir/build/BUILD/package/lib64/src/include/clRNG/lfsr113.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/mrg31k3p.clh
/builddir/build/BUILD/package/lib64/src/include/clRNG/mrg31k3p.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/mrg32k3a.clh
/builddir/build/BUILD/package/lib64/src/include/clRNG/mrg32k3a.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/philox432.clh
/builddir/build/BUILD/package/lib64/src/include/clRNG/philox432.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/private/Random123/array.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/private/Random123/features/clangfeatures.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/private/Random123/features/compilerfeatures.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/private/Random123/features/gccfeatures.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/private/Random123/features/msvcfeatures.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/private/Random123/features/open64features.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/private/Random123/features/openclfeatures.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/private/Random123/features/sse.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/private/Random123/philox.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/private/lfsr113.c.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/private/modular.c.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/private/mrg31k3p.c.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/private/mrg32k3a.c.h
/builddir/build/BUILD/package/lib64/src/include/clRNG/private/philox432.c.h
/builddir/build/BUILD/package/lib64/src/library/CMakeLists.txt
/builddir/build/BUILD/package/lib64/src/library/clRNG.c
/builddir/build/BUILD/package/lib64/src/library/clRNG.pc.in
/builddir/build/BUILD/package/lib64/src/library/clRNGConfig.cmake.in
/builddir/build/BUILD/package/lib64/src/library/lfsr113.c
/builddir/build/BUILD/package/lib64/src/library/modularHost.c.h
/builddir/build/BUILD/package/lib64/src/library/mrg31k3p.c
/builddir/build/BUILD/package/lib64/src/library/mrg32k3a.c
/builddir/build/BUILD/package/lib64/src/library/philox432.c
/builddir/build/BUILD/package/lib64/src/library/private.c
/builddir/build/BUILD/package/lib64/src/library/private.h
/builddir/build/BUILD/package/lib64/src/tests/CMakeLists.txt
/builddir/build/BUILD/package/lib64/src/tests/ctest/checks.c.h
/builddir/build/BUILD/package/lib64/src/tests/ctest/checks.h
/builddir/build/BUILD/package/lib64/src/tests/ctest/checks_prec.c.h
/builddir/build/BUILD/package/lib64/src/tests/ctest/cli.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/dispatch.c.h
/builddir/build/BUILD/package/lib64/src/tests/ctest/lfsr113_checks_d.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/lfsr113_checks_s.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/lfsr113_common.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/lfsr113_dispatch.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/mangle.h
/builddir/build/BUILD/package/lib64/src/tests/ctest/mrg31k3p_checks_d.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/mrg31k3p_checks_s.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/mrg31k3p_common.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/mrg31k3p_dispatch.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/mrg32k3a_checks_d.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/mrg32k3a_checks_s.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/mrg32k3a_common.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/mrg32k3a_dispatch.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/philox432_checks_d.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/philox432_checks_s.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/philox432_common.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/philox432_dispatch.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/util.c
/builddir/build/BUILD/package/lib64/src/tests/ctest/util.h
/builddir/build/BUILD/package/lib64/src/tests/philox432_ut.c
/builddir/build/BUILD/package/lib64/src/tests/uniform.hpp


%changelog
* Fri Aug 12 2016 Benson Muite <benson_muite@emailplus.org>
- Initial version of package
