-- =============================================================================
--        Hi there, this is **my** lunarvim config file.
--        I am currently on nvim v0.9 and lunarvim v1.3.
--                breaking changes are possible.
--  ============================================================================

----------------- General
local aiGeneratedPallettes = require("aigen")

lvim.log.level = "warn"
-- I use format on save sometimes... Depending on the project
-- So this line is everchanging
lvim.format_on_save.enabled = false
-- The GOAT ( this is literally the same as tokyonight afaik, but comes bundled with lvim)
lvim.colorscheme = "lunar"
-- lvim.colorscheme = "text-to-colorscheme"
-- Others I like
-- lvim.colorscheme = "github_dark_dimmed"
-- lvim.colorscheme = "catppuccin"
-- lvim.colorscheme = "gruvbox"
-- lvim.colorscheme = "sonokai"
-- lvim.colorscheme = "gruvbox-material"

lvim.transparent_window = true
lvim.keys.normal_mode["<S-l>"] = ":BufferLineCycleNext<CR>"
lvim.keys.normal_mode["<S-h>"] = ":BufferLineCyclePrev<CR>"


----------------- Plugins

lvim.plugins = {
  {
    'meatballs/notebook.nvim',
    config = function()
      require('notebook').setup()
    end
  },
  { 'wakatime/vim-wakatime' },
  {
    "jiaoshijie/undotree",
    dependencies = "nvim-lua/plenary.nvim",
    config = true,
    keys = { -- load the plugin only when using it's keybinding:
      { "<leader>-", "<cmd>lua require('undotree').toggle()<cr>" },
    },
  },
  {
    "iamcco/markdown-preview.nvim",
    build = "cd app && yarn install",
  },
  -- { 'github/copilot.vim' },
  {
    'norcalli/nvim-colorizer.lua',
    config = function()
      require('colorizer').setup()
    end
  },
  { 'nvim-lua/plenary.nvim' },
  {
    'ThePrimeagen/harpoon',
    config = function()
      require("harpoon").setup({})
    end
  },
  {
    "saecki/crates.nvim",
    dependencies = { "nvim-lua/plenary.nvim" },
    config = function()
      require("crates").setup()
    end
  },
  { "catppuccin/nvim",            name = "catpuccin" },
  { 'projekt0n/github-nvim-theme' },
  {
    'rose-pine/neovim',
    name = 'rose-pine',
    config = function()
      require('rose-pine').setup({
        disable_background = true
      })
    end
  },
  -- {
  --   "j-hui/fidget.nvim",
  --   config = function()
  --     require("fidget").setup()
  --   end,
  -- },
  {
    "Zeioth/markmap.nvim",
    build = "yarn global add markmap-cli",
    cmd = { "MarkmapOpen", "MarkmapSave", "MarkmapWatch", "MarkmapWatchStop" },
    opts = {
      html_output = "/tmp/markmap.html", -- (default) Setting a empty string "" here means: [Current buffer path].html
      hide_toolbar = true,               -- (default)
      grace_period = 3600000             -- (default) Stops markmap watch after 60 minutes. Set it to 0 to disable the grace_period.
    },
    config = function(_, opts) require("markmap").setup(opts) end
  },
  {
    "svermeulen/text-to-colorscheme.nvim",
    config = function()
      require("text-to-colorscheme").setup {
        ai = {
          openai_api_key = os.getenv("OPENAI_API_KEY"),
          gpt_model = "gpt-3.5-turbo-0613",
        },
        hex_palettes = aiGeneratedPallettes,
        default_palette = "starry night sky tokyo",
      }
    end
  },
  {
    'sainnhe/sonokai',
    config = function()
      -- available: 'default' 'atlantis', 'andromeda', 'shusia', 'maia', 'espresso'
      vim.g.sonokai_style = 'espresso'
      -- vim.g.sonokai_enable_italic = 1
      -- vim.g.sonokai_disable_italic_comment = 1
      vim.g.sonokai_transparent_background = lvim.transparent_window
    end
  },
  {
    'sainnhe/gruvbox-material',
    config = function()
      -- Set contrast.
      -- This configuration option should be placed before `colorscheme gruvbox-material`.
      -- Available values: 'hard', 'medium'(default), 'soft'
      vim.g.gruvbox_material_background = 'hard'

      -- For better performance
      vim.g.gruvbox_material_better_performance = 1
      vim.g.gruvbox_material_transparent_background = lvim.transparent_window
    end
  },
  {
    'ellisonleao/gruvbox.nvim',
    config = function()
      require("gruvbox").setup({
        terminal_colors = true, -- add neovim terminal colors
        undercurl = true,
        underline = true,
        bold = true,
        italic = {
          strings = true,
          emphasis = true,
          comments = true,
          operators = false,
          folds = true,
        },
        strikethrough = true,
        invert_selection = false,
        invert_signs = false,
        invert_tabline = false,
        invert_intend_guides = false,
        inverse = true,    -- invert background for search, diffs, statuslines and errors
        contrast = "soft", -- can be "hard", "soft" or empty string
        palette_overrides = {},
        overrides = {},
        dim_inactive = false,
        transparent_mode = lvim.transparent_window,
      })
    end
  }
}

----------------- Additional Plugins Setup

-- Remove tab from cmp so that it can be used for copilot
lvim.builtin.cmp.mapping["<Tab>"] = nil
lvim.builtin.cmp.mapping["<S-Tab>"] = nil

vim.g.copilot_no_tab_map = false
vim.g.copilot_assume_mapped = true
require("telescope").load_extension('harpoon')


-----------------  Keymappings

-- Move selected line / block of text in visual mode
lvim.keys.visual_mode["J"] = ":m '>+1<CR> gv=gv"
lvim.keys.visual_mode["K"] = ":m '<-2<CR> gv=gv"

-- C-f to open tmux sessionizer
lvim.keys.normal_mode["<C-f>"] = "<cmd>silent !tmux neww newtmux<CR>"

-- leader p to paste over selected text without replacing clipboard
vim.keymap.set("x", "<leader>p", [["_dP]])

-- open terminal in current buf dir
lvim.keys.normal_mode["<leader>\\"] = "<cmd>silent ToggleTerm dir='%:p:h'<CR>"

-- recenter after these
lvim.keys.normal_mode["n"] = "nzzzv"
lvim.keys.normal_mode["N"] = "Nzzzv"
lvim.keys.normal_mode["<C-d>"] = "<C-d>zz"
lvim.keys.normal_mode["<C-u>"] = "<C-u>zz"

-- harpoon mappings
lvim.keys.normal_mode["<leader>u"] = ':lua require("harpoon.ui").nav_file(1)<CR>'
lvim.keys.normal_mode["<leader>i"] = ':lua require("harpoon.ui").nav_file(2)<CR>'
lvim.keys.normal_mode["<leader>o"] = ':lua require("harpoon.ui").nav_file(3)<CR>'

-- harpoon
lvim.builtin.which_key.mappings["h"] = {
  name = "Harpoon",
  m = { ':lua require("harpoon.ui").toggle_quick_menu()<CR>', "Menu" },
  h = { ':lua require("harpoon.ui").toggle_quick_menu()<CR>', "Also Menu" },
  n = { ':lua require("harpoon.ui").nav_next()<CR>', "Next" },
  p = { ':lua require("harpoon.ui").nav_prev()<CR>', "Prev" },
  w = { ':lua require("harpoon.mark").add_file()<CR>', "Add to jump list" },
}

-----------------  Run / Build Binds
-- Rust
vim.api.nvim_create_autocmd({ "BufWinEnter" }, {
  pattern = { "*.toml", "*.rs" },
  callback = function()
    vim.keymap.set("n", "<leader>rr", "<cmd>silent !tmux neww 'cargo run & while [ : ]; do sleep 1; done'<CR>")
    vim.keymap.set("n", "<leader>rR", "<cmd>silent !tmux neww 'cargo run'<CR>")
    vim.keymap.set("n", "<leader>rt", "<cmd>silent !tmux neww 'cargo test & while [ : ]; do sleep 1; done'<CR>")
    vim.keymap.set("n", "<leader>rc", "<cmd>silent !tmux neww 'cargo check & while [ : ]; do sleep 1; done'<CR>")
    vim.keymap.set("n", "<leader>rb", "<cmd>silent !tmux neww 'cargo build & while [ : ]; do sleep 1; done'<CR>")
  end
})
-- JS/TS
vim.api.nvim_create_autocmd({ "BufWinEnter" }, {
  pattern = { "*.ts", "*.js", "*.jsx", "*.tsx" },
  callback = function()
    vim.keymap.set("n", "<leader>rr", "<cmd>silent !tmux neww 'yarn run dev & while [ : ]; do sleep 1; done'<CR>")
    vim.keymap.set("n", "<leader>rR", "<cmd>silent !tmux neww 'yarn run dev'<CR>")
    vim.keymap.set("n", "<leader>rt", "<cmd>silent !tmux neww 'yarn run test & while [ : ]; do sleep 1; done'<CR>")
    vim.keymap.set("n", "<leader>rc", "<cmd>lua print('not implemented')<CR>")
    vim.keymap.set("n", "<leader>rb", "<cmd>silent !tmux neww 'yarn run build & while [ : ]; do sleep 1; done'<CR>")
  end
})
-- Markdown
vim.api.nvim_create_autocmd({ "BufWinEnter" }, {
  pattern = { "*.md" },
  callback = function()
    vim.keymap.set("n", "<leader>rr", "<cmd>silent MarkmapOpen<CR>")
    vim.keymap.set("n", "<leader>rR", "<cmd>silent MarkdownPreview<CR>")
  end
})
-----------------  Options

vim.opt.relativenumber = true
vim.opt.tabstop = 2
vim.opt.softtabstop = 2
vim.opt.shiftwidth = 2
vim.opt.expandtab = true
vim.opt.smartindent = true

-- I don't use wraps
vim.opt.wrap = false

-- this is because the highlight stays on and it's annoying
vim.opt.hlsearch = false
vim.opt.incsearch = true

vim.opt.scrolloff = 8
-- vim.opt.relativenumber = true
vim.opt.updatetime = 50

-- vim.opt.colorcolumn = "80"

-- lvim.builtin.nvimtree.setup.view.side = "right"

-- cpp fix
-- lvim.lsp.automatic_configuration.skipped_servers.push("clangd")
local capabilities = vim.lsp.protocol.make_client_capabilities()
capabilities.offsetEncoding = { "utf-16" }
require("lspconfig").clangd.setup({ capabilities = capabilities })

-- disable alpha dashboard
lvim.builtin.alpha.active = false
