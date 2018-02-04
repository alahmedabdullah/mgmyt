if [ -d "../backend/mgmyt/tardis/apps/mongoquery/static" ]; then

    echo "cp -r ./js ../backend/mgmyt/tardis/apps/mongoquery/static"
    cp -r ./js ../backend/mgmyt/tardis/apps/mongoquery/static

    echo "cp -r ./mongoquery ../backend/mgmyt/tardis/apps/mongoquery/static"
    cp -r ./mongoquery ../backend/mgmyt/tardis/apps/mongoquery/static

fi
if [ ! -d "../backend/mgmyt/tardis/apps/mongoquery/static" ]; then

    echo "mkdir ../backend/mgmyt/tardis/apps/mongoquery/static"
    mkdir ../backend/mgmyt/tardis/apps/mongoquery/static

    echo "cp -r ./js ../backend/mgmyt/tardis/apps/mongoquery/static"
    cp -r ./js ../backend/mgmyt/tardis/apps/mongoquery/static

    echo "cp -r ./mongoquery ../backend/mgmyt/tardis/apps/mongoquery/static"
    cp -r ./mongoquery ../backend/mgmyt/tardis/apps/mongoquery/static

fi

