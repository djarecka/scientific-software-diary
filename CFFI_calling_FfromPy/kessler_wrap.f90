module kessler_wrap

  ! using a module for interoperating with C 
  use iso_c_binding, only: c_int, c_double
  ! using an original Fortran module with a subroutine we want to use 
  use module_mp_kessler 

  implicit none

contains

  ! defining a C function - binding for Fortran function
  subroutine c_kessler(t, qv, qc, qr, rho, pii ,dt_in, z, xlv, cp, &
                       EP2, SVP1, SVP2, SVP3, SVPT0, rhowater,     &
                       dz8w, RAINNC, RAINNCV,                      &
                       ids,ide, jds,jde, kds,kde,                  & 
                       ims,ime, jms,jme, kms,kme,                  & 
                       its,ite, jts,jte, kts,kte                   & 
                      ) bind(c)

    ! declaration of variables that will be passed as values 
    real(c_double), intent(in), value :: dt_in,  xlv, cp, rhowater,    &
                                         EP2,SVP1,SVP2,SVP3,SVPT0
    integer(c_int), intent(in), value :: ids,ide, jds,jde, kds,kde,    & 
                                         ims,ime, jms,jme, kms,kme,    & 
                                         its,ite, jts,jte, kts,kte
    ! declaration arrays that will be passed as pointers
    real(c_double),  intent(in)       :: rho(ims:ime,kms:kme,jms:jme), &
                                         pii(ims:ime,kms:kme,jms:jme), &
                                         dz8w(ims:ime,kms:kme,jms:jme),&
                                         z(ims:ime,kms:kme,jms:jme)
    real(c_double),  intent(inout)    :: t(ims:ime,kms:kme,jms:jme),   &
                                         qv(ims:ime,kms:kme,jms:jme),  &
                                         qc(ims:ime,kms:kme,jms:jme),  &
                                         qr(ims:ime,kms:kme,jms:jme),  &
                                         RAINNC(ims:ime,jms:jme),      &
                                         RAINNCV(ims:ime,jms:jme)

    ! calling the original Fortran function
    call kessler(t, qv, qc, qr, rho, pii, dt_in, z, xlv, cp,   &
                 EP2, SVP1, SVP2, SVP3, SVPT0, rhowater,       &
                 dz8w, RAINNC, RAINNCV,                        &
                 ids,ide, jds,jde, kds,kde,                    & 
                 ims,ime, jms,jme, kms,kme,                    & 
                 its,ite, jts,jte, kts,kte                     & 
                )

    end subroutine c_kessler
end module kessler_wrap
