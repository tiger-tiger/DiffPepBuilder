Prior distribution and random walk in SO(3) space
To understand the \(SO(3)\) group structure better, we can look at the double cover group of \(SO(3)\), the \(SU(2)\) group.

The Quaternion representation of \(SU(2)\) group can be represented by four Pauli matrices as: \begin{equation} U=a_0 \sigma_0-\dot{\mathbb{I}}\left(a_1 \sigma_1+a_2 \sigma_2+a_3 \sigma_3\right)=a_0 \sigma_0-\dot{\mathbb{I}} \boldsymbol{a} \cdot \boldsymbol{\sigma} \end{equation} where \(\sum_i a_i^2=a_0^2+\boldsymbol{a}^2=1\).

So the manifold of \(SU(2)\) group is a 3-sphere \(S^3\) in 4D Euclidean space.

Another way to write the quaternion representation is to use axis and angle by \(U = \exp \left(-\dot{\mathbb{I}} \frac{\theta}{2} \boldsymbol{n} \bullet \boldsymbol{\sigma}\right) = \left(\cos \frac{\theta}{2}, \sin \frac{\theta}{2} \cdot \boldsymbol{n}\right)\). In this way of writing the \(SO(3)\) matrix can be represented as the adjoint representation of \(SU(2)\) group:

\[e^{-\mathrm{i} \frac{\theta}{2} \boldsymbol{n} \bullet \sigma} \cdot \sigma_a \cdot e^{\mathrm{i} \frac{\theta}{2} n \bullet \sigma}=\sum_b \sigma_b \cdot\left[\overleftrightarrow{R}_{\boldsymbol{n}}(\theta)\right]_{ba}\]
Notice that \(a_i\) and \(-a_i\) correspond to the same \(SO(3)\) matrix, so we have group structure isophism: \(\mathrm{SO}(3) \simeq \mathrm{SU}(2) / \mathbb{Z}_2\).

Since the manifold of \(SU(2)\) is \(S^3\), the Haar measure of \(SU(2)\) can be represented as:

\[\begin{equation} \mathrm{d} \mu(U)=\delta\Bigg(\sqrt{\sum\nolimits*{i=0}^3 a_i^2}-1\Bigg) \prod*{i=0}^3 \mathrm{~d} a_i \end{equation}\]
On the other hand, we can parameterize the 4D coordinates as: \(\left(a_i\right)=r \cdot\left(\cos \frac{\theta}{2}, \sin \frac{\theta}{2}(\sin \vartheta \cos \phi, \sin \vartheta \sin \phi, \cos \vartheta)\right)\), so we can transform the measure in 4D coordinate space into the axis-angle space by computing the jacobian, namely

\[\begin{equation} \delta(r-1) \cdot\left|\frac{\partial\left(a_0, a_1, a_2, a_3\right)}{\partial(r, \theta, \vartheta, \phi)}\right| \cdot \mathrm{d} r \mathrm{~d} \theta \mathrm{d} \vartheta \mathrm{d} \phi=\frac{1}{2} \sin ^2 \frac{\theta}{2} \sin \vartheta \mathrm{d} \theta \mathrm{d} \vartheta \mathrm{d} \phi = \frac{1}{2} \sin ^2 \frac{\theta}{2} \mathrm{~d} \theta \cdot \mathrm{d}^2 \boldsymbol{n} \end{equation}\]
From this expression, we can know that in the axis-angle representation of the \(SU(2)\) group, the measure in angle space is proportional to \(\sin ^2 \frac{\theta}{2} = 1 - \cos \theta\), the measure in axis space is constant. Since the axis-angle representation of the \(SU(2)\) group has a two-to-one correspondence to the axis-angle representation of the \(SO(3)\) group with the same angle \(\theta\) and axis \(n\), the measure in the axis-angle representation of the \(SO(3)\) group angle space is also proportional to \(1 - \cos \theta\), and the measure in the axis space is uniform.

From another point of view, the prior distribution in the rotation angle space is proportional to \(1 - \cos \theta\), and the prior distribution in the axis space is uniform.

Now we consider the noise adding process in \(SO(3)\) space. Like the random walk in 3D space, we apply small random rotation matrix on an initial matrix iteratively. We generate three small angles from a gaussain distribution, and compose them with Lie algebra matrix to get the rotation matrix. To write it formally,

\[\begin{equation} r^{(t+1)}=\exp \left\lbrace\sum*{d=1}^3 \epsilon_d G_d\right\rbrace r^t \end{equation}\]
Specifically, we set the standard deviation of the gaussian noise to be 0.2. After a certain number of steps, we can reach the final matrix of this process, we compute the rotation angle of this final matrix relative to the initial matrix, we can get the overall distribution of the rotation angle, as in the following figure, the left figure is the single step random walk, whose angle distribution corresponds to the so called IGSO3 distribution with the same standard deviation \(\sigma = 0.2\).

\[\begin{equation} f(\omega, \sigma)=\frac{1-\cos \omega}{\pi} \sum*{l=0}^{\infty}(2 l+1) e^{-l(l+1) \sigma^2/2} \frac{\sin \left(\left(l+\frac{1}{2}\right) \omega\right)}{\sin (\omega / 2)} \end{equation}\]
The right figure is the ten steps random walk, whose angle distribution corresponds to the IGSO3 distribution with standard deviation \(\sigma = \sqrt{0.2^2 * 10} = 0.6325\).