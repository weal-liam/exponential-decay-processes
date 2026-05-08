# Exponential decay processes

# prepare to run
Open with VScode or any IDE
# In your project directory, run these commands in the terminal
# make a virtual environment
windows -> python -m venv "any name of choice"
linux -> python3 -m venv "any name of choice"

# this installs all required python libraries
pip install -r requirements.txt


# Guide
EXPONENTIAL DECAY PROCESSES
Introduction
	These are process that have a quantity decreasing at a rate proportional to its current value resulting in a rapid initial drop that slows down over time approaching zero but theoretically never does. In many natural processes like radioactive decay and data loss, change happens constantly as a continuous series of single events. For these cases, the use of differential equations helps represent dynamic relationships and model a system that tracks the change over time.
	This project will model and visualize simplified cases of the exponential decay processes of radioactivity and data loss.
Radioactive decay and data loss
	Radioactive decay is a process in which an unstable atomic nucleus loses energy by radiation. This random process follows a highly predictable exponential decay pattern provided that a large group of atoms are involved. 
	Data loss is a critical process where information is destroyed, deleted or becomes unreadable physically or logically. The exponential decay pattern it follows, the probability of data remaining intact or relevant decreases over time.
	Differential equations will help us to model and later visualize the exponential decay, see the trends and make predictions in either case. Here, the rate of change in the quantity(number), N of atoms in radioactivity and bits in data loss over time, t is proportional to the current quantity(number) of atoms/ bits present.
-\frac{\mathbit{dN}}{\mathbit{dt}}\ \mathbit{\alpha}\ \mathbit{N}
where  \frac{\mathbit{dN}}{\mathbit{dt}} is the rate of change in the number of current substances, N  and the negative represents a decrease in the number, N.
	Solving the differential equation…..
- dN/dt ∝ N
- dN/dt = λN
dN/dt = -λN
(1/N) dN = -λ dt
ln N = -λt + ln C
when t = 0, N = N₀
∴ C = ln N₀
ln N = -λt + ln N₀
ln N - ln N₀ = -λt
ln(N/N₀) = -λt
Taking natural log inverse of both sides:
N/N₀ = e^(-λt)
N(t) = N₀ e^(-λt)

Where:
N is the remaining amount after time (t)
N₀ is the initial amount at t = 0
λ is the decay factor over time

Example:
	Finding the decay factor, λ
Assuming the initial amount of the substance (number of bits/atoms) was 32
and that it will be 28 after 10 days(t = 10), hence N₀ = 32, N(10) = 28
N(t) = N₀e^(-λt)
28 = 32e^(-10λ)
28/32 = e^(-10λ)
ln(28/32) = -10λ
-λ = ln(28/32) / 10
-λ = -0.133531393 / 10
(Decay Factor) λ = 0.0134

Then formula becomes:
N(t) = 32e^(-0.0134t)

	At t = 20
N(20) = 32e^(-0.0134 × 20)
N(20) = 32e^(-0.268)
N(20) = 32 × 0.7649
N(20) = 24.48
so after 20 days, the amount remaining is approximately 24.48 units(bits/atoms)
