import sys

def write_xdmf_to_h5(xdmfdir, hdf5file):
    import dolfin as df
    # Read .xdmf mesh into a FEniCS Mesh
    mesh = df.Mesh()
    with df.XDMFFile("%s/mesh.xdmf" % xdmfdir) as infile:
        infile.read(mesh)
        
    # Read cell data to a MeshFunction (of dim n)
    n = mesh.topology().dim()
    subdomains = df.MeshFunction("size_t", mesh, n)
    with df.XDMFFile("%s/subdomains.xdmf" % xdmfdir) as infile:
        infile.read(subdomains, "subdomains")
        
    # Read facet data to a MeshFunction (of dim n-1)
    boundaries = df.MeshFunction("size_t", mesh, n-1, 0)
    with df.XDMFFile("%s/boundaries.xdmf" % xdmfdir) as infile:
        infile.read(boundaries, "boundaries")

    # Write all files into a single h5 file.
    hdf = df.HDF5File(mesh.mpi_comm(), hdf5file, "w")
    hdf.write(mesh, "/mesh")
    hdf.write(subdomains, "/subdomains")
    hdf.write(boundaries, "/boundaries") 
    hdf.close()


if __name__ =='__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--hdf5file', type=str) 
    #parser.add_argument('--xdmfdir', type=str,
    #                    default="output-xdmf") 
    #Z = parser.parse_args() 
    filename = sys.argv[1]
    write_xdmf_to_h5("output-xdmf",filename ) 
