<?php

namespace kalanis\kw_templates\Template;


/**
 * Trait TFile
 * @package kalanis\kw_templates\Template
 * Trait for loading templates from files, not from code
 */
trait TFile
{

    /**
     * @return string
     * @throws Exception
     */
    protected function loadTemplate(): string
    {
        $path = $this->templatePath();
        $result = @file_get_contents($path);
        if (false === $result) {
            throw new Exception(sprintf('Template file %s not found', $path));
        }
        return $result;
    }

    abstract protected function templatePath(): string;
}
