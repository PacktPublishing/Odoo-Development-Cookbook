odoo.define_section('ch15_r04', ['ch15_r04', 'web.Model'], function (test, mock) {
    test('FieldMany2OneButtons', function(assert, ch15_r04, model)
    {
        var fake_field_manager = {
            get_field_desc: function()
            {
                return {
                    'relation': 'res.users',
                    'domain': [],
                };
            },
            on: function() {},
            off: function() {},
            get: function() {},
            $el: jQuery(),
        },
        widget = new ch15_r04.FieldMany2OneButtons(
            fake_field_manager,
            {
                attrs: {
                    modifiers: '{}',
                    name: 'field_name',
                    widget: 'many2one_buttons',
                },
            }
        ),
        $container = jQuery('<div/>'),
        async_result = assert.async();
        mock.add(
            '/web/dataset/search_read', function()
            {
                return {
                    records: [
                        {
                            id: 1,
                            display_name: 'Administrator',
                        },
                        {
                            id: 4,
                            display_name: 'Demo user',
                        },
                    ],
                    length: 2,
                }
            }
        );
        widget.attachTo($container)
        .then(function()
        {
            widget.renderElement();
            assert.deepEqual(
                widget.$el.find('button').map(function()
                {
                    return jQuery.trim(jQuery(this).text())
                }).get(),
                ['Administrator', 'Demo user'],
                'Check if the widget shows the users we expect'
            );
            async_result();
        });
    })
});
