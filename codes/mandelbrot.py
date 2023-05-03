c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=21)

members = get_members(c, num_iterations=20)


plt.scatter(members.real, members.imag, color="black", marker=",", s=1)

plt.gca().set_aspect("equal")

plt.axis("off")

plt.tight_layout()

plt.show()
