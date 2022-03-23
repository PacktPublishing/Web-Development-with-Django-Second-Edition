#!/usr/bin/env python3

from reviews.models import Publisher

Publisher.objects.filter(Q(name__startswith="New") | Q(name__startswith="Idea"))

Publisher.objects.filter(Q(name__startswith="New") & Q(name__endswith="Publisher"))