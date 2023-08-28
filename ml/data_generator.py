import numpy as np

def get_stress_from_model(eps, C, n):
    """
    Implementation of the desired 
    non-linear stress-strain relation
    """
    return C*eps**(1.0/n) 

class StressStrainDataGenerator():
    def __init__(self, num_datapoints=101, eps_min=0.0, eps_max=1.0):
        self.num_datapoints = num_datapoints
        self.eps_min = eps_min
        self.eps_max = eps_max
        self.std_noise = 0.0

    def get_stress_strain(self, C, n, add_noise=False, eps_linear_distributed=True):
        if eps_linear_distributed:
            eps = np.linspace(self.eps_min, self.eps_max, self.num_datapoints)
        else:
            eps = np.random.uniform(self.eps_min, self.eps_max, self.num_datapoints)
            eps = np.sort(eps)
        sig = get_stress_from_model(eps, C, n)
        if add_noise:
            sig += self.get_noise(len(sig), self.std_noise)       
        return np.array([eps, sig]) 

    def shuffle_stress_strain_datasets(self, data, labels):
        shuffle_index = np.random.permutation(len(labels))
        return data[shuffle_index], labels[shuffle_index]

    def get_noise(self, num_elements, sigma):
        noise = np.random.normal(0, sigma, num_elements)
        return noise        

    def generate_stress_strain_datasets(self, num_samples=100, C_range=[5,15], n_range=[2,5], shuffle=True, add_noise=True, eps_linear_distributed=False):
        generated_stress_strain_list = []
        generated_parameters_list = []
        for index_sample in range(num_samples):
                C = np.random.uniform(C_range[0],C_range[1])
                n = np.random.uniform(n_range[0],n_range[1])
                generated_stress_strain = self.get_stress_strain(C, n, add_noise, eps_linear_distributed)
                generated_stress_strain_list.append(generated_stress_strain)
                generated_parameters_list.append(np.array([C, n]))
        data = np.array(generated_stress_strain_list)
        targets = np.array(generated_parameters_list) 
        if shuffle:
            return self.shuffle_stress_strain_datasets(data, targets)  
        else:
            return data, targets
