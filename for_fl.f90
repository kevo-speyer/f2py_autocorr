program test
implicit none
integer :: i, n
real (kind=8) :: x
real (kind=8), allocatable,dimension(:) :: a, c

n=10
allocate (a(n),c(n))

do i=1,n
    x = (i-1)*2.14/(n-1) +1.
    a(i) = sin(x)
    print*,x,a(i)
end do

call f_routine(a,n,c)

print*,""
print*, c

end program

subroutine f_routine(x,n_data,corr)
implicit none
real (kind=8), dimension(n_data), intent(in) :: x
integer, intent(in) :: n_data
real (kind=8), dimension(n_data), intent(out)  :: corr
integer ,dimension(n_data) :: n_corr
integer :: i,j
real (kind=8) :: x_mean = 0, x_var = 0

!Initailize Variables
corr = 0.  
n_corr = 0

do i=1,n_data
    x_mean = x_mean + x(i)
    x_var = x_var + x(i)**2
    do j=i,n_data
        corr(j-i+1) = corr(j-i+1) + x(i)*x(j)
        n_corr(j-i+1) = n_corr(j-i+1) + 1
    end do
end do

x_mean = x_mean / n_data
x_var = x_var / n_data - x_mean**2

corr = corr / n_corr
corr = ( corr - x_mean**2 ) / x_var

end subroutine f_routine
















