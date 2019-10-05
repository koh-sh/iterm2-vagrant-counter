#!/usr/bin/env python

import os
import json
import iterm2


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description="Vagrant Counter",
        detailed_description="Show Number of Vagrant VM",
        knobs=[],
        exemplar="[Vagrant Counter]",
        update_cadence=30,
        identifier="koh-sh.vagrant-counter"
    )

    @iterm2.StatusBarRPC
    async def vagrant_counter(knobs):
        # TODO: find better emojis
        up = "🔵 "
        down = "⚫ "

        try:
            fpath = os.environ["HOME"] + "/.vagrant.d/data/machine-index/index"
            with open(fpath, "r") as f:
                d = json.loads(f.read())
            vms = d["machines"]
            up_vms = [x for x in vms if vms[x]["state"] == "running"]
            all_machines = len(vms)
            up_machines = len(up_vms)
            return (up * up_machines) + (down * (all_machines - up_machines))
        except Exception:
            return "Cannot find Vagrant info"

    await component.async_register(connection, vagrant_counter)

iterm2.run_forever(main)
