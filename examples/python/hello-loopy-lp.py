# This is a version of hello-loopy.py that can be run through
# a loopy binary using
#
# ./loopy --lang=loopy hello-loopy-lp.py -

knl = lp.make_kernel(
        "{ [i]: 0<=i<n }",
        "out[i] = 2*a[i]")

knl = lp.add_and_infer_dtypes(knl, dict(a=np.float32))
lp_knl = lp.split_iname(knl, "i", 8, outer_tag="g.0", inner_tag="l.0")
