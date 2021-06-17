Summary

This commit fixes issues reported with long parameter lists in the mpl
drawer. The issue is that when the length of the parameters list exceeds
20 characters the mpl drawer removes the parameters. Multiple attempts
have attempted to address this issue (#2994 #3353) by just increasing
that limit. But this doesn't actually solve the problem because the
boxes are fixed width so the parameters just exceed the width of the
boxes. The proper way to fix this is to dynamically

In addition this whole problem is primarily caused because we don't
round any parameter values. This commit rounds the parameters so that we
rarely have to scale to have super wide parameter lists.
